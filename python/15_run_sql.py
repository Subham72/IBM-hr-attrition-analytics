import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///../hr_attrition.db')

sql_file = "../sql/10_jobroles_by_attrition.sql"

with open(sql_file,"r") as file:
    query = file.read()

result = pd.read_sql(query,engine)

print(result)

