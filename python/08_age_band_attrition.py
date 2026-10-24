import pandas as pd

df = pd.read_csv("../data/IBM_HR_Attrition_Enhanced.csv")

df["Age_Band"] = pd.cut( df["Age"], bins=[18, 25, 35, 45, 55, 100], labels=["18-25", "26-35", "36-45", "46-55", "56-100"])

# print(df[["Age", "Age_Band"]].head(20))

result = ( df.groupby("Age_Band").agg(Total_Employees=("Attrition","count"),Employees_Left= ("Attrition" , lambda x: (x=="Yes").sum())).reset_index() )

result["Attrition_Rate"]= (result["Employees_Left"]/result["Total_Employees"])*100

print(result[["Age_Band","Total_Employees", "Employees_Left", "Attrition_Rate"]].sort_values(by="Attrition_Rate",ascending=False))

