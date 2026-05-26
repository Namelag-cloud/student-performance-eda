"""
Student Performance Exploratory Data Analysis
---------------------------------------------

Dataset:
UCI Student Performance Dataset (Math Course)

Goal:
Explore which student, family, and lifestyle factors
appear associated with final grades (G3).

This project demonstrates:
- Data loading & cleaning
- Exploratory Data Analysis (EDA)
- Correlation analysis
- Boolean filtering
- Feature engineering
- Visualization with matplotlib
- Grouped statistical comparisons

Author: Izzy
"""

import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# LOAD DATA
# ============================================================

# Dataset uses semicolon separators instead of commas
df = pd.read_csv(
    r"C:\Users\asus\.deepface\weights\student_performance_eda\student-mat.csv",
    sep=";"
)

# ============================================================
# BASIC DATA INSPECTION
# ============================================================

print("\n================ DATASET INFO ================\n")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

# ============================================================
# FEATURE ENGINEERING
# ============================================================

# Create a boolean feature:
# Does the student have at least one parent who is a teacher?

df["teacher_parent"] = (
    (df["Mjob"] == "teacher") |
    (df["Fjob"] == "teacher")
)

# ============================================================
# CORRELATION ANALYSIS
# ============================================================

print("\n================ CORRELATIONS WITH G3 ================\n")

# Variables selected for exploratory analysis
correlations = {
    "Study Time vs Final Grade": df["studytime"].corr(df["G3"]),
    "Absences vs Final Grade": df["absences"].corr(df["G3"]),
    "Health vs Final Grade": df["health"].corr(df["G3"]),
    "Free Time vs Final Grade": df["freetime"].corr(df["G3"]),
    "Going Out vs Final Grade": df["goout"].corr(df["G3"]),
    "Workday Alcohol vs Final Grade": df["Dalc"].corr(df["G3"]),
    "Weekend Alcohol vs Final Grade": df["Walc"].corr(df["G3"]),
    "Previous Failures vs Final Grade": df["failures"].corr(df["G3"]),
    "Mother Education vs Final Grade": df["Medu"].corr(df["G3"]),
    "Father Education vs Final Grade": df["Fedu"].corr(df["G3"]),
    "Second Period Grade vs Final Grade": df["G2"].corr(df["G3"]),
    "Teacher Parent vs Final Grade": df["teacher_parent"].corr(df["G3"])
}

for label, value in correlations.items():
    print(f"{label}: {value:.3f}")

# ============================================================
# GROUPED ANALYSIS
# ============================================================

print("\n================ TEACHER PARENT ANALYSIS ================\n")

teacher_analysis = df.groupby("teacher_parent")["G3"].mean()

print("Average Final Grade (G3)")
print(teacher_analysis)

# ============================================================
# GENDER ANALYSIS
# ============================================================

print("\n================ GENDER ANALYSIS ================\n")

# Average grades by gender
gender_grades = df.groupby("sex")["G3"].mean()

print("Average Final Grade by Gender:")
print(gender_grades)

# Plot average grades by gender
plt.figure(figsize=(7, 5))

gender_grades.plot(kind="bar")

plt.title("Average Final Grade by Gender")
plt.xlabel("Gender")
plt.ylabel("Average G3")

plt.show()

# ============================================================
# ROMANTIC RELATIONSHIP ANALYSIS
# ============================================================

print("\n================ ROMANTIC RELATIONSHIP ANALYSIS ================\n")

# Compare grades based on romantic relationship status
romantic_analysis = df.groupby(["sex", "romantic"])["G3"].mean()

print("Average Final Grade by Gender and Romantic Status:")
print(romantic_analysis)

# Boxplot
plt.figure(figsize=(8, 5))

df.boxplot(column="G3", by=["sex", "romantic"])

plt.title("G3 Distribution by Gender and Romantic Status")
plt.suptitle("")

plt.xlabel("(Gender, Romantic Relationship)")
plt.ylabel("Final Grade (G3)")

plt.show()

# ============================================================
# SHARE OF ROMANTIC RELATIONSHIPS BY GENDER
# ============================================================

print("\n================ ROMANTIC SHARE ANALYSIS ================\n")

romantic_share = pd.crosstab(
    df["sex"],
    df["romantic"],
    normalize="index"
) * 100

print("Percentage of Students in Romantic Relationships:")
print(romantic_share)

# Plot romantic share
plt.figure(figsize=(7, 5))

romantic_share.plot(kind="bar")

plt.title("Romantic Relationship Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Percentage")

plt.show()

# ============================================================
# SCHOOL CHOICE REASON ANALYSIS
# ============================================================

print("\n================ SCHOOL CHOICE ANALYSIS ================\n")

reason_analysis = df.groupby("reason")["G3"].mean().sort_values(ascending=False)

print("Average Final Grade by School Choice Reason:")
print(reason_analysis)

# Boxplot for school choice reason
plt.figure(figsize=(9, 5))

df.boxplot(column="G3", by="reason")

plt.title("Final Grades by School Choice Reason")
plt.suptitle("")

plt.xlabel("Reason for Choosing School")
plt.ylabel("Final Grade (G3)")

plt.show()

# ============================================================
# INTERNET ACCESS ANALYSIS
# ============================================================

print("\n================ INTERNET ACCESS ANALYSIS ================\n")

internet_analysis = df.groupby("internet")["G3"].mean()

print("Average Final Grade by Internet Access:")
print(internet_analysis)

# Boxplot
plt.figure(figsize=(7, 5))

df.boxplot(column="G3", by="internet")

plt.title("Final Grades by Internet Access")
plt.suptitle("")

plt.xlabel("Internet Access at Home")
plt.ylabel("Final Grade (G3)")

plt.show()

# ============================================================
# VISUALIZATION 1
# Scatter Plot: Absences vs Final Grade
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["absences"],
    df["G3"],
    alpha=0.5
)

plt.title("Absences vs Final Grade")
plt.xlabel("Number of Absences")
plt.ylabel("Final Grade (G3)")

plt.show()

# ============================================================
# VISUALIZATION 2
# Scatter Plot: Study Time vs Final Grade
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["studytime"],
    df["G3"],
    alpha=0.5
)

plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time")
plt.ylabel("Final Grade (G3)")

plt.show()

# ============================================================
# VISUALIZATION 3
# Scatter Plot: Previous Failures vs Final Grade
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["failures"],
    df["G3"],
    alpha=0.5
)

plt.title("Previous Failures vs Final Grade")
plt.xlabel("Number of Previous Failures")
plt.ylabel("Final Grade (G3)")

plt.show()

# ============================================================
# VISUALIZATION 4
# Boxplot: Teacher Parent vs Final Grade
# ============================================================

plt.figure(figsize=(8, 5))

df.boxplot(
    column="G3",
    by="teacher_parent"
)

plt.title("Final Grade Distribution by Teacher Parent")
plt.suptitle("")

plt.xlabel("Has Teacher Parent")
plt.ylabel("Final Grade (G3)")

plt.show()

# ============================================================
# KEY OBSERVATIONS
# ============================================================

print("\n================ KEY OBSERVATIONS ================\n")

print("""
1. G2 (second period grade) showed the strongest
   positive correlation with G3.

2. Study time and absences showed surprisingly weak
   linear correlations with final grades.

3. Previous failures showed a noticeable negative
   relationship with G3.

4. Students with at least one teacher parent had
   slightly higher average grades.

5. Students who selected schools for reputation
   tended to perform better than students choosing
   schools primarily due to proximity or course preference.

6. Romantic relationships appeared to affect academic
   performance differently across genders.

7. Internet access showed a mild positive relationship
   with student performance.

8. Human behavior and academic outcomes are influenced
   by many interacting variables rather than one single factor.
""")