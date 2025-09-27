import requests
import pandas as pd

# Replace this with the API endpoint you copied
url = "https://data.lacity.org/api/v3/views/2nrs-mtv8/query.json"

# Optional: You can filter results using parameters (like year, crime type, etc.)
params = {
    "$limit": 5000  # You can raise this to a higher number or paginate if needed
}

# Send GET request to API
response = requests.get(url, params=params)

# Check status
if response.status_code == 200:
    data = response.json() # This gives you a Python dict or list
    # if it's a list of records, covert diretly to DataFrame
    df = pd.DataFrame(data)
    # Prints out the first few rows
    print(df.head())
else:
    print("Error fetching data:", response.status_code)