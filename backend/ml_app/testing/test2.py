
import requests
import pandas as pd

included_tag_names = []
excluded_tag_names = ["Harem"]

base_url = "https://api.mangadex.org"

tags = requests.get(
    f"{base_url}/manga/tag"
).json()

# ["391b0423-d847-456f-aff0-8b0cfc03066b", "423e2eae-a7a2-4a8b-ac03-a8351462d71d"]
included_tag_ids = [
    tag["id"]
    for tag in tags["data"]
    if tag["attributes"]["name"]["en"]
       in included_tag_names
]

# ["aafb99c1-7f60-43fa-b75f-fc9502ce29c7"]
excluded_tag_ids = [
    tag["id"]
    for tag in tags["data"]
    if tag["attributes"]["name"]["en"]
       in excluded_tag_names
]

r = requests.get(
    f"{base_url}/manga",
    params={
        "includedTags[]": included_tag_ids,
        "excludedTags[]": excluded_tag_ids,
    },
)


print([manga["id"] for manga in r.json()["data"]])

print( r.json() )
df = pd.json_normalize(r.json()['data'])



# Combine the original DataFrame with the links DataFrame
df.to_csv('manga_data2.csv', index=False)

print("CSV file created successfully.")