import psycopg2
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
print("=========================DAY 3: DATABASE DATA COLLECTION===============")
connection=psycopg2.connect(
    host="localhost",
    database="day3_databases",
    user="postgres",
    password="1234",
    port="5432"
    )
query="SELECT * FROM sales;"
df=pd.read_sql(query,connection)
print("\n-------DATA FROM POSTGRESQL------")
print(df)
connection.close()
print("\nDatabase data collected successfully.")
