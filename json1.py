# importing libraries
import os
import json
import csv

# Get a list of all JSON files in the folder.
folder_path_users = ("C:/Users/Olayinka Akerekan/Downloads/project_a/users")
folder_path_cards = ("C:/Users/Olayinka Akerekan/Downloads/project_a/cards/")


def load_json_files_from_folder(folder_path):
    """
    This group of codes are written to load json folders from the local 
    repository into the python as a list of json file types  
    """

    # opem up the filepath, look through and pick file who names ends with .json, appending to an empty list json_file
    json_files = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            json_files.append(os.path.join(folder_path, file_name))
        
    # pick up the individual json files, open them and load them into an empty list json_dat
    json_data = []
    for json_file in json_files:
        with open(json_file, "r") as f:
           json_data.append(json.load(f))
    return json_data
    
    
# Load the json data into a variable set to users 
users = load_json_files_from_folder(folder_path_users)

# Load the json data into a variable set to cards 

cards = load_json_files_from_folder(folder_path_cards)

# Take in a json and return a list of dictionary data structure for both cards and users

user_lists = []
for user in users:
    user_dict = {
        "type" : user["metadata"]["type"],
        "event_at" : user["metadata"]["event_at"],
        "event_id" : user["metadata"]["event_id"],
        "id" : user["payload"]["id"],
        "name" : user["payload"]["name"],
        "address" : user["payload"]["address"],
        "job" : user["payload"]["job"],
        "score" : user["payload"]["score"]
    }
    user_lists.append(user_dict)


card_lists = []
for card in cards:
    # Perform operations on the variable
    if card["payload"].get("user_id") is not None:
        card_dict = {
            "id": card["payload"]["id"],
            "user_id": card["payload"]["user_id"],
            "created_by_name": card["payload"]["created_by_name"],
            "updated_at": card["payload"]["updated_at"],
            "created_at": card["payload"]["created_at"],
            "active": card["payload"]["active"],
            "type": card["metadata"]["type"],
            "event_at": card["metadata"]["event_at"],
            "event_id": card["metadata"]["event_id"]
    }
    card_lists.append(card_dict)

# create csv with file names users.csv consisting of all the datas

with open('cards.csv', 'w', newline='') as csv_file:
    first = True 
    for dictionary in card_lists:
        writer = csv.writer(csv_file)
        # Write the dictionary keys as the header
        if first:
            first = False
            writer.writerow(dictionary.keys())
        # Write the dictionary values as a row
        writer.writerow(dictionary.values())

# create csv with file names users.csv consisting of all the datas
with open('users.csv', 'w', newline='') as csv_file:
    first = True 
    for dictionary in user_lists:
        writer = csv.writer(csv_file)
        # Write the dictionary keys as the header
        if first:
            first = False
            writer.writerow(dictionary.keys())
        # Write the dictionary values as a row
        writer.writerow(dictionary.values())
