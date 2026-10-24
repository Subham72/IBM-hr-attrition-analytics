import pandas as pd

df = pd.read_csv("../data/IBM_HR_Attrition_Enhanced.csv")

df["Salary_Band"] = pd.cut(df["MonthlyIncome"],
                           bins=[0, 5000, 10000, 25000], labels=["Low", 'Mid', 'High'])

result = (df.groupby(["Salary_Band"]).agg(Total_Employees=("Attrition","count"),
                    Employees_Left=("Attrition", lambda x: (x=="Yes").sum())).reset_index())

result["Attrition_Rate"] = (result["Employees_Left"]/result["Total_Employees"])*100
result = result.sort_values(by=["Attrition_Rate"],ascending=False)
print(result[["Salary_Band","Total_Employees", "Employees_Left", "Attrition_Rate"]])#.sort_values(by="Attrition_Rate",ascending=False))

