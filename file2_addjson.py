'''Create a function add_to_json that takes a filename and a dictionary as input. The
function should read the JSON data from the file, add the new dictionary to it, and
write the updated data back to the same file.
'''
import json

def add_to_json(filename, new_data):
    try:
        # Read existing JSON data from the file (if any)
        try:
            with open(filename, 'r') as file:
                existing_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        # Append the new dictionary to the existing data
        existing_data.append(new_data)

        # Write the updated data back to the file
        with open(filename, 'w') as file:
            json.dump(existing_data, file, indent=4)

        print("Data added to JSON file successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = 'jsonfile.json'
new_data = {
    "Name": "Sushan Kattel",
    "Age": 24
}

add_to_json(filename, new_data)
