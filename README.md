# Student Mental Health & Burnout Analysis

[![Tableau](https://img.shields.io/badge/Tableau-Dashboards-orange?style=flat&logo=tableau)](tableau/dashboard_links.md)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python)](requirements.txt)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=flat)]()

## 📌 Project Overview
This project provides a comprehensive analysis of student mental health and burnout using a dataset of **1,000,000 students**. By leveraging a multi-stage data pipeline and advanced feature engineering, we identify key risk factors and provide actionable business recommendations for university counseling and administration teams.

### 🎯 Key Objectives
*   **Identify** primary drivers of student burnout and academic pressure.
*   **Develop** composite KPIs (Wellbeing Index, Vulnerability Score) to quantify student risk.
*   **Triage** student populations into urgent, recommended, and monitor tiers for intervention.
*   **Visualise** insights through interactive Tableau dashboards for administrative decision-making.

---

## 📊 Tableau Dashboards
The final insights are delivered via two primary dashboards:

1.  **[Burnout Overview](https://public.tableau.com/app/profile/hirdyansh.kumar/viz/Turing_BroCodes_Student-Mental-Health-and-Burnout1/Dashboard1-BurnoutOverview?publish=yes)**: High-level metrics on burnout risk, academic pressure, and demographic distributions.
2.  **[Support & Intervention Insights](https://public.tableau.com/app/profile/hirdyansh.kumar/viz/Turing_BroCodes_Student-Mental-Health-and-Burnout/Dashboard2-SupportInterventionInsights?publish=yes)**: Deep dive into protective factors (sleep, social support) and emergency bursary triggers.

*Detailed links and screenshots can be found in the [Tableau Directory](tableau/dashboard_links.md).*

---

## 🛠️ Project Structure
```text
├── data/               # Raw and processed datasets
├── docs/               # Detailed Data Dictionary (25 columns)
├── notebooks/          # Step-by-step pipeline (Cleaning → EDA → Features)
├── reports/            # Validation charts and final outputs
├── requirements.txt    # Python dependencies
├── scripts/            # Helper functions for processing
└── tableau/            # Dashboard links and screenshots
```

---

## ⚙️ Data Pipeline
The analysis follows a rigorous 6-stage pipeline:
1.  **NB01 Extraction**: Ingesting the 1M row Kaggle dataset.
2.  **NB02 Cleaning**: Handling outliers (sleep 2-12h, age 17-30), standardising categorical values, and initial KPI creation.
3.  **NB03 Feature Engineering**: Creating the `burnout_composite` and `wellbeing_index`.
4.  **NB04 EDA**: Distribution analysis and demographic segmentation.
5.  **NB05 Statistical Analysis**: Pearson correlation and ANOVA tests for significance.
6.  **NB06 Final Prep**: Validation against original Kaggle labels and final CSV export for Tableau.

### 🧪 Engineered KPIs
*   **Burnout Composite**: Average of stress, anxiety, and depression scores.
*   **Wellbeing Index**: Weighted score of sleep, social support, and financial stability.
*   **Vulnerability Score**: A stacked risk measure (0-5) identifying students meeting multiple risk criteria.
*   **Intervention Priority Tier**: Red/Amber/Green triage labels (Urgent, Recommend, Monitor).

---

## 💡 Business Recommendations
Based on the data findings, the following university interventions are proposed:
*   **Early Warning System**: Automatic flags for students scoring ≥ 4 on the `Vulnerability Score`.
*   **Assessment Reform**: Target high-pressure courses identified by the `Academic Pressure Index` for open-book exam pilots.
*   **Sleep Hygiene Workshops**: Outreach to the 34% of students identified as "Sleep Deprived".
*   **Emergency Bursary Fast-Track**: Use the `Financial Support Need Flag` to prioritise student aid applications.
*   **Peer Mentoring**: Connect students with high `Peer Mentoring Benefit Scores` to upper-year mentors.

---

## 🚀 Getting Started
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/student-burnout-analysis.git
    ```
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the analysis**:
    Execute the notebooks in `notebooks/` sequentially (01 to 06).
4.  **Explore the data**:
    Refer to `docs/data_dictionary.md` for a complete breakdown of all 25 final features.

---

## 👥 Team BroCodes
*   Hirdyansh Kumar
*   Ayush Anand
*   Sumit Kumar Nayak
*   Oashe Mehta
*   Himanshu Mishra

---
**Course**: DVA — Data Visualisation & Analytics  
**Capstone**: Project 2
