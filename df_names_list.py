#tested dataframe separately before inserting them to the db
import pandas as pd
import json

# load data using Python JSON module
with open('names.json','r') as f:
data = json.loads(f.read())

df_names_list = pd.json_normalize(data, record_path =['names'])

print(df_names_list)