import requests
import csv

def get_manga_full_info(manga_id):
    url = f"https://api.jikan.moe/v4/manga/{manga_id}/full"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('data', {})
    else:
        print(f"Failed to fetch full manga info for ID {manga_id}. Status code: {response.status_code}")
        return None

def write_to_csv(filename, data):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        for item in data:
            writer.writerow(item)

def fetch_and_store_manga_info(start_id, end_id):
    all_manga_info = []
    for manga_id in range(start_id, end_id + 1):
        manga_info = get_manga_full_info(manga_id)
        if manga_info:
            all_manga_info.append(manga_info)
            print(f"Retrieved manga info for ID {manga_id}")
    write_to_csv('manga_info.csv', all_manga_info)
    print("All manga info stored in manga_info.csv")

# Example usage:
fetch_and_store_manga_info(1, 20000)
