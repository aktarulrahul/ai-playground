import os
import json

def read_sample_files():
    print("Reading sample.txt:")
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
    
    print("\nReading sample_data.json:")
    with open("sample_data.json", "r") as file:
        data = json.load(file)
        print("Users:")
        for user in data["users"]:
            print(f"  - {user['name']} ({user['email']}) from {user['city']}")
        print(f"Settings: {data['settings']}")

def write_new_file():
    new_data = {
        "message": "Hello from Python!",
        "timestamp": "2024-01-15",
        "numbers": [1, 2, 3, 4, 5]
    }
    
    with open("output.json", "w") as file:
        json.dump(new_data, file, indent=2)
    print("Created output.json")

def file_info():
    files = ["sample.txt", "sample_data.json", "output.json"]
    for filename in files:
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            print(f"{filename}: {size} bytes")
        else:
            print(f"{filename}: not found")

def environment_info():
    print(f"Current directory: {os.getcwd()}")
    
    venv_path = os.environ.get("VIRTUAL_ENV")
    if venv_path:
        print(f"Virtual environment: {venv_path}")
    else:
        print("No virtual environment detected")

if __name__ == "__main__":
    print("=== File I/O Demo ===\n")
    
    read_sample_files()
    print()
    
    write_new_file()
    print()
    
    file_info()
    print()
    
    environment_info() 