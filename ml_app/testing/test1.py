import requests
import pandas as pd

url = "https://mangaverse-api.p.rapidapi.com/manga/fetch"

querystring = {"page":"1","genres":"Harem,Fantasy","nsfw":"true","type":"all"}

headers = {
	"X-RapidAPI-Key": "256b948859mshbd91e52c458bfa5p1dafefjsn54d790e227e7",
	"X-RapidAPI-Host": "mangaverse-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
data = response.json().get("data", [])
if data:
    first_item = data[0]
    # Print the keys (fields) of the first item
    print("Fields in the JSON data:")
    for key in first_item.keys():
        print(key)
else:
    print("No data found in the JSON response.")

df = pd.json_normalize(response.json()['data'])

# Save DataFrame to CSV file
df.to_csv('manga_data.csv', index=False)
print("CSV file created successfully.")