
import pandas as pd
import json

# load data using Python JSON module
with open('names.json','r') as f:
 data = json.loads(f.read())

#pick names starting from highest amount
df_names_highest_amount = pd.json_normalize(data, record_path = ['names'])
dataFrame = pd.DataFrame.from_dict(df_names_highest_amount)
# sorting in descending order 
dataFrame.sort_values(by=['amount'], ascending = False, inplace = True) 

# render dataframe as html
html = dataFrame.to_html()






