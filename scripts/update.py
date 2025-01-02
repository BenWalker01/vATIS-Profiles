import os
import json
import sys
from datetime import datetime

input_dir = os.path.abspath('data')

# Get the list of filenames from the command line arguments
filenames_to_update = sys.argv[1:]

for filename in filenames_to_update:
    if filename.endswith('.json'):
        name = os.path.splitext(filename)[0]
        input_filepath = os.path.join(input_dir, filename)
        
        if not os.path.exists(input_filepath):
            print(f"File {input_filepath} does not exist.")
            continue
        
        with open(input_filepath, 'r') as file:
            data = json.load(file)
        
        current_serial = str(data.get("updateSerial", "1970010100"))
        
        current_date = current_serial[:8]
        current_serial_number = int(current_serial[8:])
        
        today_date = datetime.now().strftime("%Y%m%d")

        print(f"{current_date = }")
        print(f"{today_date = }")
        print(f"{current_serial_number = }")
        
        if current_date == today_date:
            new_serial_number = current_serial_number + 1
        else:
            new_serial_number = 1

        if new_serial_number > 99:
            print("There have been too many updates today. The script will now exit")
            sys.exit(1)
        
        update_serial = f"{today_date}{new_serial_number:02d}"
        
        update_url = f"https://raw.githubusercontent.com/BenWalker01/vATIS-Profiles/refs/heads/main/data/{name}.json"
        
        data["updateUrl"] = update_url
        data["updateSerial"] = update_serial
        
        with open(input_filepath, 'w') as file:
            json.dump(data, file, indent=2)
        
        print(f"Updated {filename} with new serial {update_serial}")