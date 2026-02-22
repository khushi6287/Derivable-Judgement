# -*- coding: utf-8 -*-

## **Derivable Judgement**

import libraries
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""Load Data"""

df = pd.read_csv("public_health_dataset.txt")
df.head(1)

"""**1. Formulate at least two hypotheses from the dataset
Hypothesis 1 (Smoking vs Diabetes)**

**H₀ (Null Hypothesis)**: Smoking has no effect on diabetes prevalence.
**H₁ (Alternative Hypothesis)**: Smoking affects diabetes prevalence.
Hypothesis 2 (Age Group vs Diabetes Rate)

**H₀:** Diabetes rate is the same across all age groups.
**H₁:** Diabetes rate differs across age groups.

**2. Calculate Confidence Intervals (Age & Weight)**
"""

# Age Confidence Interval (95%)
mean_age = df["age"].mean()
std_age = df["age"].std()
n = len(df)
z = 1.96  # for 95% confidence

ci_age = (
    mean_age - z * (std_age / np.sqrt(n)),
    mean_age + z * (std_age / np.sqrt(n))
)

ci_age

# Weight Confidence Interval (95%)
mean_weight = df["weight"].mean()
std_weight = df["weight"].std()

ci_weight = (
    mean_weight - z * (std_weight / np.sqrt(n)),
    mean_weight + z * (std_weight / np.sqrt(n))
)

ci_weight

"""**3. Find Critical Value and p-value**

For α = 0.05:


*   Critical z-value = ±1.96
*   If p-value < 0.05, reject H₀

**4. Perform z-test / t-test (Mean Comparison)**

Example: Mean Age of Diabetic vs Non-Diabetic Individuals
"""

diabetic_age = df[df["diabetes"] == True]["age"]
nondiabetic_age = df[df["diabetes"] == False]["age"]

t_stat, p_value = stats.ttest_ind(diabetic_age, nondiabetic_age)

t_stat, p_value

"""**Interpretation**

*   If p-value < 0.05 → Reject H₀
*   If p-value ≥ 0.05 → Accept H₀

**5. Chi-Square Test (Smoking Status vs Diabetes)**
"""

contingency_table = pd.crosstab(df["smoking_status"], df["diabetes"])
contingency_table

chi2, p, dof, expected = stats.chi2_contingency(contingency_table)

chi2, p

plt.figure()

smoking_diabetes = pd.crosstab(df["smoking_status"], df["diabetes"])
smoking_diabetes.plot(kind="bar")

plt.title("Smoking Status vs Diabetes")
plt.xlabel("Smoking Status")
plt.ylabel("Count")

plt.show()

"""**Interpretation**
*   p < 0.05 → Smoking and diabetes are associated
*   p ≥ 0.05 → No significant association

**6. ANOVA Test (Age Group vs Diabetes Rate)**
"""

plt.figure()

df.boxplot(column="age", by="diabetes")

plt.title("Age Distribution by Diabetes Status")
plt.suptitle("")   # Removes automatic subtitle
plt.xlabel("Diabetes")
plt.ylabel("Age")

plt.show()

plt.figure()

diabetes_rate = df.groupby("age_group")["diabetes"].mean()
diabetes_rate.plot(kind="bar")

plt.title("Diabetes Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Diabetes Proportion")

plt.show()

"""**Interpretation**
*   p < 0.05 → Diabetes rate differs across age groups
*   p ≥ 0.05 → No significant difference

**7. Covariance and Correlation (Age vs BMI)**
"""

# Covariance
cov_age_bmi = np.cov(df["age"], df["bmi"])[0,1]
cov_age_bmi

# Correlation
corr_age_bmi = df["age"].corr(df["bmi"])
corr_age_bmi

plt.figure()

plt.scatter(df["age"], df["bmi"])

plt.title("Age vs BMI")
plt.xlabel("Age")
plt.ylabel("BMI")

plt.show()