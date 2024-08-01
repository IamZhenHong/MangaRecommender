import pandas as pd
from tqdm import tqdm

# Assuming df is your DataFrame with a 'synopsis' column
df = pd.read_csv("manga_info.csv")

# Function to remove the string "[Written by MAL Rewrite]" from the synopsis field
# Function to remove the string "[Written by MAL Rewrite]" from the synopsis field
def clean_synopsis(synopsis):
    if isinstance(synopsis, str):
        return synopsis.replace('Source VIZ Media', '')
    else:
        return synopsis


# Apply the clean_synopsis function to each row in the DataFrame with a progress bar
print("Cleaning synopses...")
tqdm.pandas()
df['synopsis'] = tqdm(df['synopsis'].progress_apply(clean_synopsis), total=len(df))

# Save the DataFrame to a CSV file
print("Saving cleaned DataFrame to CSV...")
df.to_csv('manga_info.csv', index=False)

print("CSV file saved successfully.")
