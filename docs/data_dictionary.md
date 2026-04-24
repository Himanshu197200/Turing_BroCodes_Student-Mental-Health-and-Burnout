# Data Dictionary
## Student Mental Health & Burnout Analysis
**Course:** DVA — Data Visualisation & Analytics  
**Capstone:** Project 2  
**Dataset Source:** https://www.kaggle.com/datasets/ayeshasiddiqa123/student-health  
**Raw File:** student_health_raw.csv  
**Clean File:** student_health_clean.csv  
**Final File:** student_health_features.csv  
**Last Updated:** April 2026  

> This dictionary documents every column across the entire data 
> pipeline — from raw ingestion through cleaning, validation, 
> feature engineering, and final Tableau export.

## SECTION 2 — Dataset Overview Table

| Stage | File | Rows | Columns | Notebook |
|---|---|---|---|---|
| Raw | student_health_raw.csv | 1,000,000 | 20 | 01_extraction.ipynb |
| Cleaned | student_health_clean.csv | ~1,000,000 | 22 | 02_cleaning.ipynb |
| Final | student_health_features.csv | ~1,000,000 | 25 | 06_feature_engineering.ipynb |

## SECTION 3 — Column Pipeline Summary

```text
Raw (20)
  → DROP internet_usage (redundant)
  → ADD burnout_composite, stress_tier, sleep_deficit
  = Cleaned (22)
  → VALIDATE burnout_score, mental_health_index, risk_level → DROP
  → DROP anxiety_score, depression_score (absorbed into burnout_composite)
  → ADD 8 engineered features
  = Final CSV (25)
```

## SECTION 4 — Raw Dataset Columns (20 columns)

### `age`
| Property | Value |
|---|---|
| Group | Demographics |
| Data Type | Numerical (continuous) |
| Range / Values | 17 – 30 |
| Description | Student age in years |
| Business Relevance | Low variance in student population. Retained for segmentation completeness. |
| Cleaning Action | Outliers outside 17-30 removed. Missing filled with median. |

### `gender`
| Property | Value |
|---|---|
| Group | Demographics |
| Data Type | Categorical |
| Range / Values | Male / Female / Other |
| Description | Student gender identity |
| Business Relevance | Gender-based mental health disparities drive counselling programme design. t-test in NB04 compares male vs female burnout. |
| Cleaning Action | Stripped whitespace, title case applied. Mapped M→Male, F→Female, MALE→Male, FEMALE→Female. |

### `academic_year`
| Property | Value |
|---|---|
| Group | Demographics |
| Data Type | Ordinal categorical |
| Range / Values | Year 1 / Year 2 / Year 3 / Year 4 |
| Description | Current year of study |
| Business Relevance | Core segmentation dimension. ANOVA in NB04 tests whether burnout significantly differs across years. Drives the "target Year 3/4" recommendation. |
| Cleaning Action | Mapped '1'→'Year 1', 'Year1'→'Year 1' etc. Standardised to consistent format. |

### `study_hours_per_day`
| Property | Value |
|---|---|
| Group | Academics |
| Data Type | Numerical (continuous) |
| Range / Values | 0 – 18 |
| Description | Average daily study hours reported by student |
| Business Relevance | U-curve finding — both under-studying AND over-studying increases stress. Drives academic advisor policy recommendation. Used in academic_pressure_index formula. |
| Cleaning Action | Outliers outside 0-18 removed. Missing filled with median. |

### `exam_pressure`
| Property | Value |
|---|---|
| Group | Academics |
| Data Type | Ordinal categorical |
| Range / Values | Low / Medium / High |
| Description | Perceived pressure from upcoming examinations |
| Business Relevance | Assessment reform lever. High exam_pressure students are prime targets for open-book or continuous assessment policy change. Used in academic_pressure_index formula (weight 35%). |
| Cleaning Action | Stripped, title case. Mapped Moderate→Medium, Mild→Low, Extreme→High. |

### `academic_performance`
| Property | Value |
|---|---|
| Group | Academics |
| Data Type | Ordinal categorical |
| Range / Values | Poor / Average / Good / Excellent |
| Description | Self-reported or assessed academic performance level |
| Business Relevance | Primary outcome variable. Proves burnout causes grade drops — the financial business case for intervention investment. Used in vulnerability_score and financial_support_need_flag. |
| Cleaning Action | Stripped, title case applied. |

### `stress_level`
| Property | Value |
|---|---|
| Group | Core Mental Health |
| Data Type | Numerical (continuous) |
| Range / Values | 0 – 10 |
| Description | Self-reported stress score (0=none, 10=extreme) |
| Business Relevance | One of three inputs to burnout_composite. Retained individually for stress_tier segmentation and Tableau filter dimension. |
| Cleaning Action | Outliers outside 0-10 removed. Missing filled with median. |

### `anxiety_score`
| Property | Value |
|---|---|
| Group | Core Mental Health |
| Data Type | Numerical (continuous) |
| Range / Values | 0 – 10 |
| Description | Self-reported anxiety score (0=none, 10=extreme) |
| Business Relevance | Input to burnout_composite. DROPPED from final CSV because fully absorbed — keeping it alongside burnout_composite creates multicollinearity. |
| Cleaning Action | Outliers outside 0-10 removed. Missing filled with median. Dropped before final export in NB06. |

### `depression_score`
| Property | Value |
|---|---|
| Group | Core Mental Health |
| Data Type | Numerical (continuous) |
| Range / Values | 0 – 10 |
| Description | Self-reported depression score (0=none, 10=extreme) |
| Business Relevance | Input to burnout_composite. DROPPED from final CSV — same reason as anxiety_score. |
| Cleaning Action | Outliers outside 0-10 removed. Missing filled with median. Dropped before final export in NB06. |

### `social_support`
| Property | Value |
|---|---|
| Group | Core Mental Health |
| Data Type | Numerical (continuous) |
| Range / Values | 0 – 10 |
| Description | Perceived level of social support from peers, family, and university (0=none, 10=strong) |
| Business Relevance | Key PROTECTIVE FACTOR. Inversely linked to burnout. Every unit increase measurably reduces depression. Drives peer mentoring programme recommendation. Used in wellbeing_index (40% weight) and peer_mentoring_benefit_score. |
| Cleaning Action | Outliers outside 0-10 removed. Missing filled with median. |

### `sleep_hours`
| Property | Value |
|---|---|
| Group | Lifestyle |
| Data Type | Numerical (continuous) |
| Range / Values | 2 – 12 |
| Description | Average daily sleep hours |
| Business Relevance | Most actionable lifestyle lever. Students below 7 hours show significantly higher anxiety. Universities can run sleep hygiene workshops immediately. Input to wellbeing_index, sleep_quality_score, sleep_deficit, and vulnerability_score. |
| Cleaning Action | Outliers outside 2-12 removed. Missing filled with median. |

### `physical_activity`
| Property | Value |
|---|---|
| Group | Lifestyle |
| Data Type | Ordinal categorical |
| Range / Values | None / Low / Moderate / High |
| Description | Level of regular physical activity |
| Business Relevance | Lifestyle segmentation dimension in Tableau. Students with None physical activity likely show higher burnout. Retained for filter use. |
| Cleaning Action | Stripped, title case applied. |

### `screen_time`
| Property | Value |
|---|---|
| Group | Lifestyle |
| Data Type | Numerical (continuous) |
| Range / Values | 0 – 16 |
| Description | Average daily screen time in hours (excluding study) |
| Business Relevance | Lifestyle context dimension. Retained after internet_usage was dropped. Used as Tableau filter to segment high screen-time students. |
| Cleaning Action | Outliers outside 0-16 removed. Missing filled with median. |

### `internet_usage`
| Property | Value |
|---|---|
| Group | Lifestyle |
| Data Type | Numerical (continuous) |
| Range / Values | 0 – 16 |
| Description | Average daily internet usage hours |
| Business Relevance | DROPPED — Pearson r > 0.85 with screen_time. Keeping both causes multicollinearity. screen_time is retained as the more interpretable measure. |
| Cleaning Action | Dropped in NB02 Step 5 after correlation check. |

### `financial_stress`
| Property | Value |
|---|---|
| Group | Pressures |
| Data Type | Numerical (continuous) |
| Range / Values | 0 – 10 |
| Description | Perceived financial pressure (0=none, 10=extreme) |
| Business Relevance | Direct university intervention lever — bursaries, payment plans, emergency aid. Strongest link to depression_score in correlation analysis. Used in wellbeing_index (20%), vulnerability_score, and financial_support_need_flag. |
| Cleaning Action | Outliers outside 0-10 removed. Missing filled with median. |

### `family_expectation`
| Property | Value |
|---|---|
| Group | Pressures |
| Data Type | Ordinal categorical |
| Range / Values | Low / Medium / High |
| Description | Perceived pressure from family regarding academic achievement |
| Business Relevance | Cultural pressure dimension. High family expectation students need counselling programme design that addresses family dynamics — especially first-generation university students. Used in academic_pressure_index (20% weight). |
| Cleaning Action | Stripped, title case applied. |

### `burnout_score`
| Property | Value |
|---|---|
| Group | Kaggle Originals |
| Data Type | Numerical (continuous) |
| Range / Values | Depends on Kaggle formula |
| Description | Kaggle's own burnout calculation. Formula not publicly documented. |
| Business Relevance | Used ONLY to cross-validate our burnout_composite in NB06. If Pearson r >= 0.7 between this and burnout_composite, our methodology is independently validated. DROPPED after validation — never in final CSV. |
| Cleaning Action | Retained through cleaning. Dropped in NB06 after cross-validation cell. |

### `mental_health_index`
| Property | Value |
|---|---|
| Group | Kaggle Originals |
| Data Type | Numerical (continuous) |
| Range / Values | Depends on Kaggle formula |
| Description | Kaggle's composite mental health index. Likely measures distress (higher = worse). |
| Business Relevance | Used ONLY to cross-validate our wellbeing_index in NB06. Expected NEGATIVE correlation confirms our index correctly measures the inverse construct. DROPPED after validation. |
| Cleaning Action | Retained through cleaning. Dropped in NB06 after cross-validation cell. |

### `risk_level`
| Property | Value |
|---|---|
| Group | Kaggle Originals |
| Data Type | Categorical |
| Range / Values | Low / Medium / High (or similar) |
| Description | Kaggle's risk categorisation label |
| Business Relevance | Used ONLY to cross-validate our intervention_priority_tier in NB06 via crosstab. Pearson not applicable — categorical comparison only. DROPPED after validation. |
| Cleaning Action | Retained through cleaning. Dropped in NB06 after cross-validation cell. |

### `dropout_risk`
| Property | Value |
|---|---|
| Group | Kaggle Originals |
| Data Type | Binary or ordinal |
| Range / Values | 0/1 or Low/High |
| Description | Kaggle's forward-looking dropout risk prediction for each student |
| Business Relevance | KEPT in final CSV — it is the only forward-looking column in the entire dataset. All other columns measure current mental state. This predicts a future event. Validates vulnerability_score. Enables unique Tableau chart: "dropout risk by academic year". |
| Cleaning Action | Missing filled with mode. Retained through all notebooks including final export. |

## SECTION 5 — Dropped Columns with Reasons

| Column | Dropped In | Reason |
|---|---|---|
| `internet_usage` | NB02 Step 5 | Pearson r > 0.85 with screen_time — redundant, causes multicollinearity |
| `anxiety_score` | NB06 Cell 16 | Fully absorbed into burnout_composite — keeping alongside creates multicollinearity in Tableau |
| `depression_score` | NB06 Cell 16 | Same as anxiety_score — absorbed into burnout_composite |
| `burnout_score` | NB06 Cell 4 | Kaggle original — used for validation only, then dropped to avoid duplicate burnout columns in Tableau |
| `mental_health_index` | NB06 Cell 5 | Kaggle original — used for validation only, then dropped |
| `risk_level` | NB06 Cell 6 | Kaggle original — used for validation only, then dropped |

## SECTION 6 — Derived KPI Columns from NB02 (3 columns)

### `burnout_composite`
| Property | Value |
|---|---|
| Group | Derived KPI (NB02) |
| Data Type | Numerical (continuous) |
| Range / Values | 0.00 – 10.00 |
| Formula | (stress_level + anxiety_score + depression_score) / 3 |
| Description | Primary KPI. Single composite score combining all three mental health dimensions into one interpretable number. |
| Business Relevance | Every Tableau chart references this column. KPI card headline metric. Used in burnout_risk_flag, vulnerability_score, wellbeing_index sanity check, and peer_mentoring_benefit_score. |
| Created In | 02_cleaning.ipynb Step 9 |

### `stress_tier`
| Property | Value |
|---|---|
| Group | Derived KPI (NB02) |
| Data Type | Ordinal categorical |
| Range / Values | Low (0-3) / Medium (4-6) / High (7-10) |
| Formula | pd.cut(stress_level, bins=[-0.01,3,6,10]) |
| Description | Segments students into 3 risk tiers based on stress_level score |
| Business Relevance | Powers the heatmap chart (Chart 8) and colour-coding across Tableau dashboards. Used as proxy for intervention_priority_tier in Validation 3 of NB06. |
| Created In | 02_cleaning.ipynb Step 10 |

### `sleep_deficit`
| Property | Value |
|---|---|
| Group | Derived KPI (NB02) |
| Data Type | Binary categorical |
| Range / Values | Sleep Deprived (<7hrs) / Adequate Sleep (>=7hrs) |
| Formula | sleep_hours < 7 → Sleep Deprived |
| Description | Classifies students by whether they meet the medically recommended minimum of 7 hours sleep |
| Business Relevance | Simple binary Tableau filter. Used alongside sleep_quality_score for sleep-focused charts. The 7-hour threshold is the WHO/NHS recommended adult minimum. |
| Created In | 02_cleaning.ipynb Step 11 |

## SECTION 7 — Validate-then-Drop Columns

These 3 Kaggle columns (`burnout_score`, `mental_health_index`, `risk_level`) exist in student_health_clean.csv but are NEVER exported to student_health_features.csv. They exist solely to prove our engineered features are methodologically valid.
See NB06 Cells 4, 5, and 6 for validation code and charts.
Validation charts saved to data/processed/:
  - validation1_burnout.png
  - validation2_wellbeing.png
  - validation3_risklevel.png

## SECTION 8 — Final Engineered Features from NB06 (8 columns)

### `burnout_risk_flag`
| Property | Value |
|---|---|
| Created In | 06_feature_engineering.ipynb Cell 8 |
| Data Type | Binary integer (0 or 1) |
| Range / Values | 0 = Not at risk / 1 = At risk |
| Formula | burnout_composite >= 6.5 → 1, else → 0 |
| Inputs Used | burnout_composite |
| Business Action | Powers KPI card "% Students at Burnout Risk" |
| Tableau Usage | KPI card, filter dimension |

### `wellbeing_index`
| Property | Value |
|---|---|
| Created In | 06_feature_engineering.ipynb Cell 9 |
| Data Type | Numerical (continuous) |
| Range / Values | 0.00 – 10.00 (higher = better) |
| Formula | (sleep_hours/12×10)×0.4 + social_support×0.4 + (10-financial_stress)×0.2 |
| Inputs Used | sleep_hours, social_support, financial_stress |
| Business Action | Inverse of burnout — measures how well a student is doing. Sleep and social support weighted highest because Pearson analysis shows strongest protective correlation. |
| Tableau Usage | KPI card, scatter plot vs burnout_composite |

### `academic_pressure_index`
| Property | Value |
|---|---|
| Created In | 06_feature_engineering.ipynb Cell 10 |
| Data Type | Numerical (continuous) |
| Range / Values | Approx 0 – 10 |
| Formula | exam_pressure_score×0.35 + study_hours×0.30 + family_expectation_score×0.20 + year_pressure_score×0.15 |
| Inputs Used | exam_pressure, study_hours_per_day, family_expectation, academic_year |
| Business Action | Single index identifying students under extreme combined academic pressure — more powerful than any one column alone. |
| Tableau Usage | Scatter plot vs burnout_composite, bar chart by academic_year |

### `vulnerability_score`
| Property | Value |
|---|---|
| Created In | 06_feature_engineering.ipynb Cell 11 |
| Data Type | Integer count |
| Range / Values | 0 – 5 |
| Formula | Count of conditions met simultaneously: sleep_hours < 7 (1 point), financial_stress >= 7 (1 point), burnout_composite >= 6 (1 point), social_support < 4 (1 point), academic_performance in [Poor, Average] (1 point) |
| Inputs Used | sleep_hours, financial_stress, burnout_composite, social_support, academic_performance |
| Business Action | Stacked risk measure. Score 4-5 = immediate counsellor referral. More powerful than any single threshold. |
| Tableau Usage | Bar chart distribution, filter for high-risk student lists |

### `intervention_priority_tier`
| Property | Value |
|---|---|
| Created In | 06_feature_engineering.ipynb Cell 12 |
| Data Type | Ordinal categorical |
| Range / Values | Tier 1: Urgent / Tier 2: Recommend / Tier 3: Monitor |
| Formula | vulnerability_score >= 4 → Tier 1: Urgent, vulnerability_score 2-3 → Tier 2: Recommend, vulnerability_score 0-1 → Tier 3: Monitor |
| Inputs Used | vulnerability_score |
| Business Action | Most actionable column in the project. Converts data science output into a label a counselling team can act on without understanding the underlying model. |
| Tableau Usage | Colour dimension on EVERY chart |

### `sleep_quality_score`
| Property | Value |
|---|---|
| Created In | 06_feature_engineering.ipynb Cell 13 |
| Data Type | Numerical (continuous) |
| Range / Values | 0.00 – 10.00 (higher = better) |
| Formula | 7-9 hrs → 10.0 (optimal) <br> < 7 hrs → 10 - (7 - hours) × 1.5 <br> > 9 hrs → 10 - (hours - 9) × 1.0 |
| Inputs Used | sleep_hours |
| Business Action | More nuanced than raw sleep_hours. Enables "sleep quality" KPI card distinct from "sleep hours" chart. |
| Tableau Usage | KPI card, histogram, scatter vs anxiety_score |

### `financial_support_need_flag`
| Property | Value |
|---|---|
| Created In | 06_feature_engineering.ipynb Cell 14 |
| Data Type | Binary integer (0 or 1) |
| Range / Values | 0 = No immediate need / 1 = Needs support |
| Formula | financial_stress >= 7 AND academic_performance in [Poor, Average] → 1 |
| Inputs Used | financial_stress, academic_performance |
| Business Action | Fast-track bursary application trigger. Most directly actionable flag in the dataset. |
| Tableau Usage | KPI card "Students needing emergency bursary", bar chart by academic_year |

### `peer_mentoring_benefit_score`
| Property | Value |
|---|---|
| Created In | 06_feature_engineering.ipynb Cell 15 |
| Data Type | Numerical (continuous) |
| Range / Values | 0.00 – 10.00 (higher = more benefit) |
| Formula | (10 - social_support)×0.50 + burnout_composite×0.30 + academic_pressure_index×0.20 |
| Inputs Used | social_support, burnout_composite, academic_pressure_index |
| Business Action | Score >= 8 = ideal peer mentor candidate. Isolated + overwhelmed + pressured students benefit most from an upper-year mentor connection. Can prevent dropout. |
| Tableau Usage | Ranked list chart, scatter vs dropout_risk |

## SECTION 9 — Final CSV Column List (25 columns confirmed)

| # | Column | Type | Source | Notebook |
|---|---|---|---|---|
| 1 | `age` | Numerical | Raw | NB01 |
| 2 | `gender` | Categorical | Raw → Standardised | NB02 |
| 3 | `academic_year` | Ordinal | Raw → Standardised | NB02 |
| 4 | `study_hours_per_day` | Numerical | Raw | NB02 |
| 5 | `academic_performance` | Ordinal | Raw → Standardised | NB02 |
| 6 | `exam_pressure` | Ordinal | Raw → Standardised | NB02 |
| 7 | `stress_level` | Numerical | Raw | NB02 |
| 8 | `social_support` | Numerical | Raw | NB02 |
| 9 | `sleep_hours` | Numerical | Raw | NB02 |
| 10 | `physical_activity` | Ordinal | Raw → Standardised | NB02 |
| 11 | `screen_time` | Numerical | Raw | NB02 |
| 12 | `financial_stress` | Numerical | Raw | NB02 |
| 13 | `family_expectation` | Ordinal | Raw → Standardised | NB02 |
| 14 | `dropout_risk` | Binary/Ordinal | Kaggle original | NB02 |
| 15 | `burnout_composite` | Numerical | Derived | NB02 |
| 16 | `stress_tier` | Ordinal | Derived | NB02 |
| 17 | `sleep_deficit` | Categorical | Derived | NB02 |
| 18 | `burnout_risk_flag` | Binary | Engineered | NB06 |
| 19 | `wellbeing_index` | Numerical | Engineered | NB06 |
| 20 | `academic_pressure_index` | Numerical | Engineered | NB06 |
| 21 | `vulnerability_score` | Integer | Engineered | NB06 |
| 22 | `intervention_priority_tier` | Ordinal | Engineered | NB06 |
| 23 | `sleep_quality_score` | Numerical | Engineered | NB06 |
| 24 | `financial_support_need_flag` | Binary | Engineered | NB06 |
| 25 | `peer_mentoring_benefit_score` | Numerical | Engineered | NB06 |

## SECTION 10 — Business Recommendations Reference

| Feature | Business Recommendation | University Action |
|---|---|---|
| `burnout_risk_flag` | Recommendation 1: Early warning system | Flag at-risk students each semester for counsellor outreach |
| `wellbeing_index` | Recommendation 1: Baseline wellness tracking | Track wellbeing_index trend per student across years |
| `academic_pressure_index` | Recommendation 2: Assessment reform | Target high-pressure students for open-book exam pilots |
| `vulnerability_score` | Recommendation 3: Multi-factor intervention | Score >= 4 triggers automatic counsellor referral |
| `intervention_priority_tier` | All recommendations | Red/Amber/Green triage system for counselling team |
| `sleep_quality_score` | Recommendation 4: Sleep hygiene programme | Workshop invitation for students scoring below 6 |
| `financial_support_need_flag` | Recommendation 5: Emergency bursary fast-track | Flag = 1 triggers priority bursary application review |
| `peer_mentoring_benefit_score` | Recommendation 6: Peer mentoring programme | Score >= 8 = assign upper-year peer mentor |
