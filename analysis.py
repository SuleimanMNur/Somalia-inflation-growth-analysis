import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Finding CSV files in the project
csv_files = list(Path(".").rglob("*.csv"))

print("CSV files found:", csv_files)

# Load the first CSV file
df = pd.read_csv(csv_files[0])

# Showing the dataset
print("\nFirst five observations:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nDescriptive statistics:")
print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())

# Descriptive statistics for economic variables

print("\nEconomic Summary Statistics:")

print(df[["inflation", "gdp_growth"]].describe())

# # Correlation between inflation and GDP growth

correlation = df["inflation"].corr(df["gdp_growth"])

print("\nCorrelation between Inflation and GDP Growth:")
print(correlation)


# Chart 1: Economic trends over time

plt.figure(figsize=(10, 5))

plt.plot(df["year"], df["inflation"],
         marker="o", label="inflation (%)")

plt.plot(df["year"], df["gdp_growth"],
         marker="s", label="gdp growth (%)")

plt.title("Somalia: Inflation and GDP Growth (2013–2023)")
plt.xlabel("Year")
plt.ylabel("Percentage (%)")
plt.legend()
plt.grid(True)

plt.savefig("charts/economic_trends.png",
            dpi=300, bbox_inches="tight")

plt.show()


# Chart 2: Scatter plot

plt.figure(figsize=(8, 5))

plt.scatter(df["inflation"], df["gdp_growth"])

plt.title("Inflation and GDP Growth in Somalia")
plt.xlabel("Inflation (%)")
plt.ylabel("GDP Growth (%)")
plt.grid(True)

plt.savefig("charts/inflation_growth_scatter.png",
            dpi=300, bbox_inches="tight")

plt.show()


# Define independent and dependent variables
X = df["inflation"]
Y = df["gdp_growth"]

# Add the intercept (constant)
X = sm.add_constant(X)

# Estimate OLS regression
model = sm.OLS(Y, X).fit()

# Display regression results
print("\nOLS REGRESSION RESULTS")
print(model.summary())

# Save regression summary

with open("regression_results.txt", "w") as file:
    file.write(model.summary().as_text())

print("Regression results saved successfully!")