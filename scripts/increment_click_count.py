import json
import os

# Path to the count file
count_file_path = 'download_count.json'

# Load the current count
if os.path.exists(count_file_path):
    with open(count_file_path, 'r') as f:
        data = json.load(f)
        download_count = data.get('count', 0)
else:
    download_count = 0

# Increment the count
download_count += 1

# Save the new count
with open(count_file_path, 'w') as f:
    json.dump({'count': download_count}, f)

print(f'Download count updated to: {download_count}')
