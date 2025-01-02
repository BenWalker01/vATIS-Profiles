import os
import json
from datetime import datetime

profiles_dir = 'profiles'
update_serial = datetime.now().strftime("%Y%m%d01")

for filename in os.listdir(profiles_dir):
    if filename.endswith('.json'):
        name = os.path.splitext(filename)[0]
        filepath = os.path.join(profiles_dir, filename)
        with open(filepath, 'r') as file:
            data = json.load(file)
        
        update_url = f"https://raw.githubusercontent.com/BenWalker01/vATIS-Profiles/refs/heads/main/{name}.json"
        
        # Add updateUrl and updateSerial under the Name field
        if "Name" in data:
            data["updateUrl"] = update_url
            data["updateSerial"] = str(update_serial)  # Ensure updateSerial is a string
        
        # Write the updated data back to the file
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=2)
        
        print(f"Updated {filename}")