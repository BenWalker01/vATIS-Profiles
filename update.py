import os
import json
from datetime import datetime

input_dir = 'data'
output_dir = 'profiles'
update_serial = int(datetime.now().strftime("%Y%m%d00"))


for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
        name = os.path.splitext(filename)[0]
        input_filepath = os.path.join(input_dir, filename)
        output_filepath = os.path.join(output_dir, filename)
        
        with open(input_filepath, 'r') as file:
            data = json.load(file)
        
        update_url = f"https://raw.githubusercontent.com/BenWalker01/vATIS-Profiles/refs/heads/main/data/{name}.json"
        
        new_data = {
            "Name": data.get("Name",name),
            "updateUrl": update_url,
            "updateSerial": update_serial,
            "stations": data.get("stations", [])
        }
        
        # Write the updated data to the output file
        with open(input_filepath, 'w') as file:
            json.dump(new_data, file, indent=2)
        
        print(f"Updated {filename}")