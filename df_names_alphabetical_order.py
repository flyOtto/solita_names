#tested dataframe separately before inserting them to the db
import pandas as pd
import json

df_names_alphabetical = pd.json_normalize(data, record_path = ['names'])
df_names_alphabetical_order = df_names_alphabetical.sort_values('name')

print(df_names_alphabetical_order)