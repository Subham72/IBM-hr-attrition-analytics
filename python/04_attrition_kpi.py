import pandas as pd

df = pd.read_csv("../data/IBM_HR_Attrition_Enhanced.csv")

total_employees = len(df)

employees_left = len(df[df["Attrition"]== "Yes"])

attrition_rate = (employees_left / total_employees) * 100

print("Total Employees : " , total_employees)
print("Total Employees left : " , employees_left)
print("Attrition Rate : " ,round(attrition_rate,2), "%")


