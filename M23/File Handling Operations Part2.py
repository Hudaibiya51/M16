import json

# Writing JSON data to a file
def write_json_to_file(file_name, data):
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        print(f"JSON data written to {file_name}")

# Reading JSON data from a file
def read_json_from_file(file_name):
    try:
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
            print(f"Read JSON data: {data}")
    except FileNotFoundError:
        print(f"{file_name} not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")

# Example usage:
data = {"name": "Alice", "age": 25, "city": "New York"}
write_json_to_file('data.json', data)
read_json_from_file('data.json')
