# Turing_BroCodes_Student-Mental-Health-and-Burnout

[![Tableau](https://img.shields.io/badge/Tableau-Dashboards-orange?style=flat&logo=tableau)](tableau/dashboard_links.md)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python)](requirements.txt)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=flat)]()

## Project Overview
| Field | Details |
|---|---|
| **Project Title** | Student Mental Health and Burnout Analysis |
| **Sector** | EdTech / Higher Education |
| **Team ID** | Turing_BroCodes |
| **Section** | DVA |
| **Faculty Mentor** | Deepali Ma'am, Vrushali Ma'am, Kajal Ma'am |
| **Institute** | Newton School of Technology |
| **Submission Date** | 28 April 2026 |

## Team Members
| Role | Name | GitHub Username |
|---|---|---|
| Project Lead & Full-Stack Analyst | Himanshu Mishra | [Himanshu197200](https://github.com/Himanshu197200) |
| BI & Visualisation Engineer | Ayush Anand | [AyushAnand-28](https://github.com/AyushAnand-28) |
| Data Analyst | Hirdyansh Kumar | [HirdyanshKumar](https://github.com/HirdyanshKumar) |
| Statistical Modeler | Sumit Kumar Nayak | [Sumit210106](https://github.com/Sumit210106) |
| Research & Documentation Lead | Oashe Mehta | [Oashe02](https://github.com/Oashe02) |

## Business Problem
**Sector Context**: The Higher Education sector is currently experiencing a widely documented mental health crisis. With rising tuition costs, highly competitive job markets, and the isolating effects of modern digital lifestyles, students are exhibiting record-high levels of clinical anxiety and depression. Universities are heavily incentivized—both ethically and financially—to ensure student wellbeing, as student dropout directly correlates with massive losses in tuition revenue and institutional prestige.

**Core Business Question**: How can a university utilize demographic, academic, and lifestyle data to predictively segment their 1,000,000-student population into precise risk tiers, enabling proactive, targeted interventions rather than reactive crisis management?

**Decision Supported**: This analysis enables university counseling and administration departments to shift from a "first-come, first-served" reactive model to a proactive, data-driven triage model, automatically triggering financial aid, targeted counseling, and peer mentorship for high-risk students.

## Dataset
| Attribute | Details |
|---|---|
| **Source Name** | Kaggle ("Student Mental Health Analysis Dataset") |
| **Direct Access Link** | [Dataset Link](https://www.kaggle.com/datasets/ayeshasiddiqa123/student-health/data) |
| **Row Count** | 1,000,000 |
| **Column Count** | 20 raw features (reduced and optimized during ETL) |
| **Time Period Covered** | Cross-sectional snapshot |
| **Format** | CSV |

**Key Columns Used**
| Column Name | Description | Role in Analysis |
|---|---|---|
| `Stress Level` | Self-reported stress indicator | Used to calculate Burnout Composite |
| `Exam Pressure` | Pressure from academic assessments | Used to calculate Burnout Composite |
| `Sleep Quality` | Self-reported quality of sleep | Key threshold indicator for stress penalty |
| `Financial Stress` | Level of financial difficulty | Used to calculate Vulnerability Score & trigger aid |
| `Social Support` | Level of peer/family support | Acts as a buffer against high exam pressure |
| `Study Hours` | Number of hours spent studying | Used to identify the "Over-Study Penalty" |

*For full column definitions, see `docs/data_dictionary.md`.*

## KPI Framework
| KPI | Definition | Formula / Computation |
|---|---|---|
| **Burnout Composite (1-10 Scale)** | A weighted metric calculating total mental exhaustion. | `(Stress × 0.4) + (Exam Pressure × 0.4) + ((10 − Sleep Quality) × 0.2)` |
| **Vulnerability Score (1-10 Scale)** | A holistic lifestyle and socio-economic risk metric. | `(Financial Stress × 0.4) + (Academic Pressure × 0.4) + ((10 − Social Support) × 0.2)` |
| **Intervention Priority Tier** | Categorical segmentation mapping students to action plans. | Tier 1: Urgent (Red)<br>Tier 2: Recommend (Orange)<br>Tier 3: Monitor (Green) |

## Tableau Dashboard
| Item | Details |
|---|---|
| **Dashboard URL** | 1. [Burnout Overview](https://public.tableau.com/app/profile/hirdyansh.kumar/viz/Turing_BroCodes_Student-Mental-Health-and-Burnout1/Dashboard1-BurnoutOverview?publish=yes)<br>2. [Support & Intervention Insights](https://public.tableau.com/app/profile/hirdyansh.kumar/viz/Turing_BroCodes_Student-Mental-Health-and-Burnout/Dashboard2-SupportInterventionInsights?publish=yes) |
| **Executive View** | **Burnout Overview**: High-level metrics on burnout risk, academic pressure, and demographic distributions. |
| **Operational View** | **Support & Intervention Insights**: Deep dive into protective factors (sleep, social support) and emergency bursary triggers. |
| **Main Filters** | Demographic segmentation, risk tiers, and specific vulnerability factors. |

## Key Insights
1. **Sleep Threshold Breaches**: Sleep deprivation is the primary early warning indicator. Students falling below 7 hours exhibit a compounding stress penalty (+2.5 point baseline jump).
2. **Financial Trigger Point**: Financial stress remains manageable until a critical threshold at Level 7 (out of 10), after which vulnerability to dropout skyrockets exponentially.
3. **The Over-Study Penalty**: There is no "sweet spot" for extreme academic dedication; stress levels increase strictly and aggressively as study hours increase, leading directly to burnout (Polynomial Degree 2 curve).
4. **Social Support as Buffer**: High social support (Levels 8-10) demonstrably neutralizes the negative impacts of high exam pressure.
5. **Gender-Agnostic Risk**: Mental health vulnerability is completely systemic; Male, Female, and Other students exhibit identical burnout rates, meaning interventions do not need demographic tailoring.
6. **The Compounding Effect of Bursaries**: Students flagged with high financial need account for the majority of the Tier 1 Intervention group, indicating that financial aid is fundamentally a mental health intervention.
7. **Academic Year Uniformity**: Burnout remains uniformly high across all Academic Years (1-4), dismantling the myth that only Freshmen require targeted resources.
8. **Predictable Isolation**: Students lacking both financial aid and peer mentoring exhibit a 3x higher likelihood of entering the Urgent Tier.
9. **Extracurricular Exhaustion**: Participation in extracurricular activities shows diminishing returns on wellbeing; exceeding 10 hours per week transitions the activity from a positive social buffer to a significant burnout accelerator.
10. **The Mid-Semester Peak**: The velocity of burnout score acceleration dramatically increases during the mid-semester period, indicating that proactive counseling interventions must be front-loaded in the first 6 weeks of the term rather than waiting for final exam crises.

## Recommendations
| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| **1** | Financial Trigger Point & Compounding Bursaries | **Automated Financial Interventions**: Implement an automated proactive bursary trigger for any student whose internal financial stress indicators breach Level 7. | Targets the root cause for the majority of Tier 1 students and reduces financial dropout vulnerability. |
| **2** | Sleep Threshold Breaches | **Campus-Wide "Sleep Hygiene" Mandate**: Invest in sleep-awareness campaigns and strictly limit late-night academic deadlines (e.g., locking submission portals at 10 PM). | Lowers the highly significant stress baseline penalty (+2.5 points) associated with <7 hours of sleep. |
| **3** | Social Support as Buffer | **Expansion of Peer-Mentorship Programs**: Divert funding to scale structured peer-mentoring events, utilizing social support as the ultimate protective factor against burnout. | Decreases the likelihood of students entering the Urgent Tier by neutralizing exam pressure. |
| **4** | Gender-Agnostic Risk & Uniformity | **Counseling Resource Reallocation**: Shift from a "first-come, first-served" model to a triage model utilizing the Intervention Priority Tier, targeting high-risk students universally. | Maximizes the impact of counseling resources and drives a conservative dropout reduction of 15-20% among at-risk students. |
| **5** | The Over-Study Penalty & Mid-Semester Peak | **Curriculum Pacing and Assessment Restructuring**: Mandate the de-escalation of "winner-take-all" final exams and distribute academic weight into smaller, continuous assessments. | Flattens mid-semester study-hour spikes that trigger severe Tier 1 burnout and mitigates the over-study penalty. |

## 🛠️ Project Structure
```text
DVA_Turing_BroCodes_Student-Mental-Health-and-Burnout/
|
|-- README.md
|-- requirements.txt
|
|-- data/
|   |-- raw/                         # Markdown link to download raw dataset
|   |   `-- raw_data_link.md
|   `-- processed/                   # Cleaned output from ETL pipeline
|       |-- *.csv                    # Cleaned data and KPI features
|       `-- *.png                    # EDA charts and Statistical analysis
|
|-- notebooks/
|   |-- 01_extraction.ipynb
|   |-- 02_cleaning.ipynb
|   |-- 03_feature_engineering.ipynb
|   |-- 04_eda.ipynb
|   |-- 05_statistical_analysis.ipynb
|   `-- 06_final_load_prep.ipynb
|
|-- scripts/
|   `-- etl_pipeline.py
|
|-- tableau/
|   |-- screenshots/
|   |-- dashboard_links.md
|   `-- Turing_BroCodes_Student-Mental-Health-and-Burnout.twbx
|
|-- reports/
|   `-- Turing_BroCodes_Student-Mental-Health-and-Burnout.pdf
|
`-- docs/
    `-- data_dictionary.md
```

## ⚙️ Data Pipeline & Methodology
The analysis follows a rigorous 6-stage pipeline:
1.  **NB01 Extraction**: Ingesting the 1M row Kaggle dataset.
2.  **NB02 Cleaning**: Handling outliers (sleep 2-12h, age 17-30), missing values (median imputation), dropping redundant native scores, memory optimization (downcasting), standardising categorical values, and initial KPI creation.
3.  **NB03 Feature Engineering**: Creating the `burnout_composite` and `vulnerability_score`.
4.  **NB04 EDA**: Univariate, Bivariate, and Multivariate analysis (e.g., distribution analysis, correlation heatmaps).
5.  **NB05 Statistical Analysis**: Pearson correlation, variance testing across Gender, regression analysis on Study Hours vs Stress (Polynomial Degree 2), and ANOVA tests.
6.  **NB06 Final Prep**: Validation against original labels and final CSV export for Tableau.

## 🚀 Getting Started
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Himanshu197200/Turing_BroCodes_Student-Mental-Health-and-Burnout.git
    ```
2.  **Install dependencies**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
3.  **Run the analysis**:
    Execute the notebooks in `notebooks/` sequentially (01 to 06).
4.  **Explore the data**:
    Refer to `docs/data_dictionary.md` for a complete breakdown of all features.

## Contribution Matrix
| Team Member | Role | Dataset and Sourcing | ETL and Cleaning | EDA and Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT and Viva |
|---|---|---|---|---|---|---|---|---|
| Himanshu Mishra | Project Lead & Full-Stack Analyst | Owner | Owner | Support | Support | Owner | Owner | Support |
| Ayush Anand | BI & Visualisation Engineer | Support | Support | Support | Support | Owner | Support | Support |
| Hirdyansh Kumar | Data Analyst | Support | Support | Owner | Support | Support | Support | Support |
| Sumit Kumar Nayak | Statistical Modeler | Support | Support | Support | Owner | Support | Support | Support |
| Oashe Mehta | Research & Documentation Lead | Support | Support | Support | Support | Support | Owner | Owner |

*Declaration: We confirm that the above contribution details are accurate and verifiable through GitHub Insights, PR history, and submitted artifacts.*

