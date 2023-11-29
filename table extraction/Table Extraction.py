#Table Extraction - Extract tables from Websites
import pandas as pd 
import camelot.io as camelot
#pip install camelot-py
#dependencies for camelot :pip install ghostscript pip install tk
# simpsons = pd.read_html("https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(season_21%E2%80%93present)")
# print(len(simpsons))
# print(simpsons[0].head())
# #Table Extraction - Extract CSV Files from Websites
# premier_21=pd.read_csv("https://www.football-data.co.uk/mmz4281/2324/E0.csv")
# print(premier_21.head())
# premier_21.rename(columns={"FTHG":"Home_goals","FTAG":"Away_goals"},inplace=True)
# print(premier_21.head())
# #Table Extraction - Extract Tables from pdfs
tables=camelot.read_pdf("C:\\Users\\fnac\\Documents\\studies\\S3\\P2\\ab-elementary-school-rankings-2023-15552.pdf",pages="17",flavor="stream")
print(tables)

tables[0].to_excel("UPWORK1.xlsx")