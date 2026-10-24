import pandas as pd

df = pd.read_csv("../data/IBM_HR_Attrition_Enhanced.csv")

result = (df.groupby("JobRole").agg(Total_Employees=("Attrition","count"),Employees_Left=("Attrition", lambda x: (x=="Yes").sum() )).reset_index())

result["Attrition_Rate"] = (result["Employees_Left"]/result["Total_Employees"])*100

result = result.sort_values(by="Attrition_Rate",ascending=False)

print(result)