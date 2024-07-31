import pandas as pd
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from tqdm import tqdm

# Load the CSV file into a DataFrame
df = pd.read_csv('all_manga.csv')

# Function to scrape description from a URL asynchronously
async def scrape_description(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()  # Raise an exception for HTTP errors
            html_content = await response.text()
            soup = BeautifulSoup(html_content, 'html.parser')
            description_tag = soup.find('span', itemprop='description')
            if description_tag:
                return description_tag.text.strip()
            else:
                return "Description not found"
    except aiohttp.ClientError as e:
        return f"Error fetching data from {url}: {e}"
    except Exception as e:
        return f"Error: {e}"

# Main function to scrape descriptions asynchronously
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [scrape_description(session, url) for url in df['page_url']]
        descriptions = await asyncio.gather(*tasks)
        df['description'] = descriptions

# Run the main function asynchronously
tqdm.pandas()  # Enable tqdm progress bar for pandas apply function
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# Save the updated DataFrame to a new CSV file
df.to_csv('MAL-manga-with-description.csv', index=False)

print("Descriptions scraped and added to the CSV file.")
