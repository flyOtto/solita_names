#tested dataframe separately before inserting them to the db
import pandas as pd
import json

df_names_highest_amount = pd.json_normalize(data, record_path = ['names'])
dataFrame = pd.DataFrame.from_dict(df_names_highest_amount)
# sorting in descending order 
dataFrame.sort_values(by=['amount'], ascending = False, inplace = True) 

print(dataFrame)