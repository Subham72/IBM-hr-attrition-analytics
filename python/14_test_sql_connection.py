from idlelib import query
from unittest import result

import pandas as pd
from sqlalchemy import create_engine, Select

engine = create_engine('sqlite:///../hr_attrition.db')

query="""
Select *
from employees
Limit 5
"""
result = pd.read_sql(query, engine)
print(result)

