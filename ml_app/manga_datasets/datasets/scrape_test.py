import requests
from bs4 import BeautifulSoup

url = "https://myanimelist.net/manga/792/City_Hunter"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the <span itemprop="description"> tag
    description_tag = soup.find('span', itemprop='description')
    
    # Extract description text
    if description_tag:
        description = description_tag.text.strip()
        print("Description:", description)
    else:
        print("Description not found on the page.")
else:
    print("Failed to retrieve HTML content. Status code:", response.status_code)
