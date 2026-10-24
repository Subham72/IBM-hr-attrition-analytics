import pandas as pd

df = pd.read_csv("../data/IBM_HR_Attrition_Enhanced.csv")

df["Age_Band"] = pd.cut(df["Age"], bins=[18, 25, 35, 45, 55, 100], labels=["18-25", "26-35", "36-45", "46-55", "56-100"])

df["Salary_Band"] = pd.cut(df["MonthlyIncome"], bins=[0, 5000, 10000, 25000], labels=["0-5000", "1000-10000", "2500-10000"])

df["Attrition_Flag"] = (df["Attrition"] == "Yes").astype(int)

df.to_csv("../data/HR_Attrition_Dashboard_Data.csv", index=False)

print("Dashboard data exported successfully")