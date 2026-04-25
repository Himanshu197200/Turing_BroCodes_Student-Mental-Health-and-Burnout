"""
ETL Pipeline Script
Project: Student Mental Health & Burnout Analysis
Description: Standalone Python script version of the cleaning pipeline.
             All transformation logic from 02_cleaning.ipynb is 
             consolidated here for reproducibility.
Author: [Team Member Name]
Date: April 2026
"""

import pandas as pd
import numpy as np
import os

RAW_PATH = '../data/raw/student_health_raw.csv'
PROCESSED_PATH = '../data/processed/student_health_clean.csv'

transformation_log = []

def log(step, action, detail, rows_affected=None):
    """Helper function to format and store transformation logs"""
    entry = f"[STEP {step:02d}] {action}"
    if rows_affected is not None:
        entry += f" | Rows affected: {rows_affected:,}"
    if detail:
        entry += f"\n         Detail: {detail}"
    transformation_log.append(entry)
    print(entry)

def load_data(path):
    """Load raw dataset and return DataFrame"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Raw dataset not found at {path}. Please ensure it exists.")
    
    df = pd.read_csv(path, low_memory=False)
    
    memory_mb = df.memory_usage(deep=True).sum() / (1024 * 1024)
    print(f"Data Loaded: {df.shape[0]:,} rows x {df.shape[1]} columns ({memory_mb:.2f} MB)")
    
    return df

def clean_data(df):
    """Execute full cleaning pipeline — returns cleaned DataFrame"""
    initial_rows = len(df)
    
    df.drop_duplicates(inplace=True)
    dupes_dropped = initial_rows - len(df)
    log(1, "Remove duplicate rows", "Dropped exact match duplicates", rows_affected=dupes_dropped)
    
    num_cols = ['age', 'study_hours_per_day', 'stress_level', 'anxiety_score',
                'depression_score', 'sleep_hours', 'social_support', 'screen_time',
                'internet_usage', 'financial_stress']
    cat_cols = ['gender', 'academic_year', 'exam_pressure', 'academic_performance',
                'physical_activity', 'family_expectation', 'risk_level', 'dropout_risk']
    
    for col in num_cols:
        median_val = df[col].median()
        df[col].fillna(median_val, inplace=True)
        log(2, f"Fill missing values ({col})", f"Filled with MEDIAN: {median_val}")
        
    for col in cat_cols:
        mode_val = df[col].mode()[0]
        df[col].fillna(mode_val, inplace=True)
        log(2, f"Fill missing values ({col})", f"Filled with MODE: {mode_val}")

    df['gender'] = df['gender'].astype(str).str.strip().str.title()
    df['gender'].replace({'M': 'Male', 'F': 'Female'}, inplace=True)
    log(3, "Standardise categorical values (gender)", "Mapped 'M'/'F' to 'Male'/'Female'")
    
    df['academic_year'] = df['academic_year'].astype(str).str.strip().str.title()
    year_map = {'1.0': 'Year 1', '1': 'Year 1', 'Year1': 'Year 1',
                '2.0': 'Year 2', '2': 'Year 2', 'Year2': 'Year 2',
                '3.0': 'Year 3', '3': 'Year 3', 'Year3': 'Year 3',
                '4.0': 'Year 4', '4': 'Year 4', 'Year4': 'Year 4'}
    df['academic_year'] = df['academic_year'].replace(year_map)
    log(3, "Standardise categorical values (academic_year)", "Standardised to 'Year X' format")
    
    df['exam_pressure'] = df['exam_pressure'].astype(str).str.strip().str.title()
    df['exam_pressure'].replace({'Moderate': 'Medium', 'Mild': 'Low', 'Extreme': 'High'}, inplace=True)
    log(3, "Standardise categorical values (exam_pressure)", "Mapped synonyms to Low/Medium/High")
    
    df['academic_performance'] = df['academic_performance'].astype(str).str.strip().str.title()
    log(3, "Standardise categorical values (academic_performance)", "Stripped whitespace and title cased")
    
    df['physical_activity'] = df['physical_activity'].astype(str).str.strip().str.title()
    log(3, "Standardise categorical values (physical_activity)", "Stripped whitespace and title cased")
    
    df['family_expectation'] = df['family_expectation'].astype(str).str.strip().str.title()
    log(3, "Standardise categorical values (family_expectation)", "Stripped whitespace and title cased")

    valid_ranges = {
        'age': (17, 30),
        'study_hours_per_day': (0, 18),
        'stress_level': (0, 10),
        'anxiety_score': (0, 10),
        'depression_score': (0, 10),
        'sleep_hours': (2, 12),
        'social_support': (0, 10),
        'screen_time': (0, 16),
        'internet_usage': (0, 16),
        'financial_stress': (0, 10)
    }
    
    for col, (min_val, max_val) in valid_ranges.items():
        before_count = len(df)
        df = df[(df[col] >= min_val) & (df[col] <= max_val)]
        dropped = before_count - len(df)
        log(4, f"Remove outliers ({col})", f"Valid range: {min_val} - {max_val}", rows_affected=dropped)

    corr = df['internet_usage'].corr(df['screen_time'])
    print(f"Correlation between internet_usage and screen_time: {corr:.3f}")
    df.drop(columns=['internet_usage'], inplace=True)
    log(5, "Drop internet_usage", f"Dropped due to high correlation with screen_time (r={corr:.3f})")

    return df

def derive_features(df):
    """Derive burnout_composite, stress_tier, sleep_deficit columns"""
    df['burnout_composite'] = (df['stress_level'] + df['anxiety_score'] + df['depression_score']) / 3
    df['burnout_composite'] = df['burnout_composite'].round(2)
    print(f"FEATURE 1: burnout_composite | Range: {df['burnout_composite'].min()} - {df['burnout_composite'].max()} | Mean: {df['burnout_composite'].mean():.2f}")
    
    bins = [-0.01, 3, 6, 10]
    labels = ['Low', 'Medium', 'High']
    df['stress_tier'] = pd.cut(df['stress_level'], bins=bins, labels=labels)
    print(f"\nFEATURE 2: stress_tier value counts:\n{df['stress_tier'].value_counts()}")
    
    df['sleep_deficit'] = np.where(df['sleep_hours'] < 7, 'Sleep Deprived (<7hrs)', 'Adequate Sleep (>=7hrs)')
    print(f"\nFEATURE 3: sleep_deficit value counts:\n{df['sleep_deficit'].value_counts()}")
    
    return df

def export_data(df, path):
    """Export cleaned DataFrame to processed folder"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    df.to_csv(path, index=False)
    
    df_check = pd.read_csv(path, nrows=5)
    
    file_size_mb = os.path.getsize(path) / (1024 * 1024)
    
    print(f"\nEXPORT SUMMARY:")
    print(f"Path   : {path}")
    print(f"Rows   : {len(df):,}")
    print(f"Columns: {df.shape[1]}")
    print(f"Size   : {file_size_mb:.2f} MB")
    
if __name__ == "__main__":
    df = load_data(RAW_PATH)
    df = clean_data(df)
    df = derive_features(df)
    export_data(df, PROCESSED_PATH)
    
    print("=" * 55)
    print("  ETL PIPELINE COMPLETE")
    print("=" * 55)
    print(f"  Input rows    : 1,000,000 (raw)")
    print(f"  Output rows   : {df.shape[0]:,}")
    print(f"  Output columns: {df.shape[1]}")
    print(f"  Expected cols : 22")
    print(f"  Column check  : {'PASS' if df.shape[1]==22 else 'FAIL'}")
    print(f"  Null check    : {'PASS' if df.isnull().sum().sum()==0 else 'FAIL'}")
    print(f"  Duplicate check: {'PASS' if df.duplicated().sum()==0 else 'FAIL'}")
    print(f"\n  Transformations logged: {len(transformation_log)}")
