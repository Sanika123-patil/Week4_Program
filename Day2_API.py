import requests
import pandas as pd
print("==================DAY 2 : API DATA COLLECTION====================")
#API URL
url="https://jsonplaceholder.typicode.com/users"
#Send request to API
response=requests.get(url)
print("\n----STATUS CODE-----")
print(response.status_code)
#Convert API response into JSON
data=response.json()
print("\n--- JSON RESPONSE----")
print(data)
#Convert JSON data into DataFrame
df=pd.DataFrame(data)
print("\n------ DATAFRAME-------")
print(df)
#Save API data as JSON file
df.to_json("day2_api_data.json",orient="records")
print("\nAPI data collected successfully.")
