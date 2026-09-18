import pandas as pd
print("================DAY 1:DATA COLLECTION FROM FILES========")
#CSV
csv_df= pd.read_csv("Sales.csv")
print("\n---CSV DATA ---")
print(csv_df)
#Excel
excel_df= pd.read_excel("Sales.xlsx",skiprows=1, usecols="B:F")
print("\n-----EXCEL DATA-----")
print(excel_df)
#JSON
json_df=pd.read_json("Sales.json")
print("\n---JSON DATA---")
print(json_df)
print("\nCSV, Excel and JSON data loaded successfully.")
