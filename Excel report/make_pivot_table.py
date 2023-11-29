import pandas as pd
df = pd.read_excel("supermarket_sales.xlsx")
#Select the columns I'll use ion the pivot table
df = df[["Gender","Product line","Total"]]
#Make pivot table with the sum of the total sales
pivot_table=df.pivot_table(index='Gender',columns='Product line',values='Total',aggfunc='sum').round(0)
#Save the pivot table in a new Excel file
pivot_table.to_excel("pivot_table.xlsx","report",startrow=4,startcol=4)