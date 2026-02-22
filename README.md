# 🏥 Derivable Judgement: Statistical Decision-Making Model

## 📖 Project Overview

This project is a comprehensive statistical analysis of public health data, designed to apply **inferential statistics** and **hypothesis testing** to real-world health scenarios. As a data analyst at a public health research organization, I analyzed health records to derive judgements about significant factors affecting disease occurrence, specifically **Diabetes**.

The project demonstrates the practical application of various statistical techniques including hypothesis testing, confidence intervals, t-tests, chi-square tests, ANOVA, and correlation analysis.

**Project File**: `derivable_judgement.py`
**Dataset**: `public_health_dataset.txt`

---

## 🎯 Objective

The main objectives of this project are:
- To apply **inferential statistics** to evaluate multiple hypotheses
- To understand and implement various **statistical tests** (t-test, chi-square, ANOVA)
- To calculate and interpret **confidence intervals** for key variables
- To analyze **correlation and covariance** between health variables
- To make **data-driven decisions** about factors affecting diabetes
- To visualize data for better understanding and interpretation

---

## 📊 Dataset Description

The dataset contains health records of individuals with the following attributes:

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| record_id | String | Unique identifier for each health record |
| age_group | String | Age group category (18-25, 26-35, 36-45, 46-60, 60+) |
| age | Integer | Age of individuals (years) |
| weight | Integer | Weight of individual (kg) |
| gender | String | Gender (Male, Female, Other) |
| region | String | Geographic region (North, South, East, West) |
| smoking_status | String | Smoking habit (Smoker, Non-Smoker, Former Smoker) |
| exercise_frequency | String | Exercise frequency (Daily, Weekly, Rarely, Never) |
| bmi | Float | Body Mass Index |
| blood_pressure | Float | Systolic blood pressure (mmHg) |
| diabetes | Boolean | Diabetes diagnosis (True/False) |
| hypertension | Boolean | Hypertension diagnosis (True/False) |
| cholesterol_level | Float | Total cholesterol level (mg/dL) |
| glucose_level | Float | Fasting glucose level (mg/dL) |
| visit_date | Date | Date of health check-up |

**Dataset Size**: 200+ records

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Primary programming language |
| **Google Colab** | Development environment |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computations |
| **SciPy** | Statistical tests and functions |
| **Matplotlib** | Data visualization |
| **Git/GitHub** | Version control and hosting |

---

## 📚 Theoretical Concepts Covered

### 1. **Inferential Statistics**
Using sample data to make conclusions about a larger population. In this project, we use health records from 200+ individuals to make inferences about the general population.

### 2. **Hypothesis Testing**
A method to test claims using data with the following components:
- **Null Hypothesis (H₀)**: No effect or difference (e.g., Smoking has no effect on diabetes)
- **Alternative Hypothesis (H₁)**: There is an effect or difference (e.g., Smoking affects diabetes)
- **Significance Level (α)**: Usually 0.05 (5% risk of being wrong)
- **Test Statistic**: Calculated from sample data (t-statistic, chi-square, etc.)
- **p-value**: Probability of obtaining results if H₀ is true

### 3. **Confidence Intervals**
A range of values within which the true population parameter is likely to fall. For example, a 95% confidence interval means we are 95% confident that the true population mean lies within that range.

### 4. **p-value Interpretation**
- **p < 0.05**: Reject H₀ (statistically significant result)
- **p ≥ 0.05**: Fail to reject H₀ (not statistically significant)

### 5. **Type I and Type II Errors**
- **Type I Error (False Positive)**: Rejecting a true null hypothesis
- **Type II Error (False Negative)**: Failing to reject a false null hypothesis

### 6. **Statistical Tests Used**
- **t-test**: Compares means between two groups (e.g., age of diabetics vs non-diabetics)
- **Chi-square test**: Tests relationship between categorical variables (e.g., smoking and diabetes)
- **ANOVA**: Compares means across three or more groups (e.g., diabetes rate across age groups)

### 7. **Covariance and Correlation**
- **Covariance**: Measures the directional relationship between two variables
- **Correlation**: Measures both strength and direction of relationship (-1 to +1)

---

## 📝 Hypotheses Formulated

### Hypothesis 1: Smoking vs Diabetes
- **H₀ (Null Hypothesis)**: Smoking has no effect on diabetes prevalence
- **H₁ (Alternative Hypothesis)**: Smoking affects diabetes prevalence
- **Test Used**: Chi-square test
- **Variables**: smoking_status (categorical), diabetes (boolean)

### Hypothesis 2: Age Group vs Diabetes Rate
- **H₀**: Diabetes rate is the same across all age groups
- **H₁**: Diabetes rate differs across age groups
- **Test Used**: ANOVA (visual analysis)
- **Variables**: age_group (categorical), diabetes (boolean)

### Additional Analysis: Age Difference between Diabetic and Non-Diabetic
- **H₀**: Mean age is same for diabetics and non-diabetics
- **H₁**: Mean age differs between diabetics and non-diabetics
- **Test Used**: Independent t-test
- **Variables**: age (continuous), diabetes (boolean)

### Correlation Analysis: Age vs BMI
- **H₀**: No correlation between age and BMI
- **H₁**: Significant correlation exists between age and BMI
- **Test Used**: Pearson correlation
- **Variables**: age (continuous), bmi (continuous)

---

## 🔬 Statistical Tests Performed

| # | Hypothesis | Test Used | Variables | Code Implementation |
|---|------------|-----------|-----------|---------------------|
| 1 | Smoking affects diabetes | Chi-square test | smoking_status, diabetes | `stats.chi2_contingency()` |
| 2 | Age differs by diabetes status | Independent t-test | age, diabetes | `stats.ttest_ind()` |
| 3 | Diabetes rate differs by age group | ANOVA (visual) | age_group, diabetes | Grouped bar chart |
| 4 | Age correlates with BMI | Pearson correlation | age, bmi | `df['age'].corr(df['bmi'])` |

---

## 📊 Key Findings

### 1. **Confidence Intervals**
- **Age**: 95% CI [lower_bound, upper_bound]
- **Weight**: 95% CI [lower_bound, upper_bound]
- *Interpretation*: We are 95% confident that the true population mean lies within these ranges

### 2. **T-Test Results (Age: Diabetic vs Non-Diabetic)**
- **t-statistic**: [value from your output]
- **p-value**: [value from your output]
- **Conclusion**: [Reject/Fail to reject] H₀
- **Interpretation**: [There is/is not] significant evidence that age differs between diabetic and non-diabetic individuals

### 3. **Chi-Square Test Results (Smoking vs Diabetes)**
- **Chi-square statistic**: [value from your output]
- **p-value**: [value from your output]
- **Conclusion**: [Reject/Fail to reject] H₀
- **Interpretation**: [There is/is not] significant association between smoking status and diabetes

### 4. **ANOVA Analysis (Age Groups vs Diabetes)**
- **Visual Analysis**: Bar chart shows diabetes proportion across age groups
- **Interpretation**: Diabetes rate [increases/decreases/varies] with age

### 5. **Correlation Analysis (Age vs BMI)**
- **Covariance**: [value from your output]
- **Correlation coefficient**: [value from your output]
- **Interpretation**: [Positive/Negative/No] correlation between age and BMI

----------


---

## 🚀 How to Run

### Prerequisites
- Python 3.8 or higher
- Google Colab account (recommended) or Jupyter Notebook
- Required libraries: pandas, numpy, scipy, matplotlib

### Method 1: Run in Google Colab (Recommended)

1. **Open Google Colab**
   - Go to [colab.research.google.com](https://colab.research.google.com)

2. **Upload Files**
   - Click the folder icon on the left sidebar
   - Click upload (📤) and upload:
     - `public_health_dataset.txt`
     - `derivable_judgement.py`

3. **Create a New Notebook**
   - Click File → New Notebook
   - Copy and paste the code from `derivable_judgement.py` into cells
   - OR upload the .py file and run: `%run derivable_judgement.py`

4. **Run the Code**
   - Press `Shift + Enter` to run each cell
   - Or click Runtime → Run all

