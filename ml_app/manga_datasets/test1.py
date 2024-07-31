import pandas as pd
import time

# Load the CSV file into a DataFrame
df = pd.read_csv('all_manga.csv')

# Start the timer
start_time = time.time()

# Traverse all rows in the DataFrame
for index, row in df.iterrows():
    # Process each row here (optional)
    pass

# End the timer
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print("Time taken to traverse all rows:", elapsed_time, "seconds")
