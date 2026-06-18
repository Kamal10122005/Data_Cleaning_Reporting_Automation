import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("raw_data.csv")

print("Original Data:")
print(df)

# Remove duplicates
df = df.drop_duplicates(subset=["Name", "Age", "Salary"])
print("\nData Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())


# Handle missing values
df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\nCleaned Data:")
print(df)

# Create reports folder if not exists
os.makedirs("reports", exist_ok=True)

# Save cleaned data
df.to_excel("reports/cleaned_data.xlsx", index=False)

# Generate summary report
summary = df.describe(include="all")
summary.to_excel("reports/summary_report.xlsx")

# Create visualization
plt.figure(figsize=(6,4))
plt.bar(df["Name"], df["Salary"])
plt.title("Salary Report")
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.tight_layout()

plt.savefig("reports/salary_chart.png")
plt.show()

print("\nProject Completed Successfully!")
plt.figure(figsize=(6,4))
df["Age"].plot(kind="hist", bins=5)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.tight_layout()

plt.savefig("reports/age_distribution.png")