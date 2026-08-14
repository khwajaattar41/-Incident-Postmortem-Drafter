import os

def read_incident_log(file_path):
    if not os.path.exists(file_path):
        return "No incident log found."

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()