import pandas as pd

df = pd.read_csv("../data/IBM_HR_Attrition_Enhanced.csv")

department_attrition = (df.groupby("Department")["Attrition"]
                        .apply(lambda x : (x=="Yes").sum()).reset_index()
                        )

department_attrition.columns = ["Department", "employees_left"]

print(department_attrition)