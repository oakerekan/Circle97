"""
What we were given 

Two json folders
users information
cards information 

get the data into python,

Create relationship with drawsql 
python and SQL

manipulate into python dictionary
reconstructed into a csv file

take the CSV from python into Dbeaver and intend to answer the question 
we were given  
"""

import os
import json
import pandas as pd

# Get a list of all JSON files in the folder.
folder_path_users = ("C:/Users/Olayinka Akerekan/Desktop/altschool/events/events/users/")
folder_path_cards = ("C:/Users/Olayinka Akerekan/Desktop/altschool/events/events/cards/")


def load_json_files_from_folder(folder_path):
    """This group of codes are written to load json folders from the local 
    repository into the python as a list of json file types  
    """
    json_files = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            json_files.append(os.path.join(folder_path, file_name))
        

    json_data = []
    for json_file in json_files:
        with open(json_file, "r") as f:
           json_data.append(json.load(f))
    return json_data
    
    
# Load the json data into a variable set to users 
users = load_json_files_from_folder(folder_path_users)

# Load the json data into a variable set to cards 

cards = load_json_files_from_folder(folder_path_cards)


# for card in cards:
#     print(card)
#     print("-"*40)

# users_dict = {
#     "type" : user["metadata"]["type"], "event_at" : user["metadata"]["event_at"] for user in users}
    
#     # "event_at" : user["metadata"]["event_at"],
#     # "event_id" : user["metadata"]["event_id"],
#     # "id" : user["payload"]["id"],
#     # "name" : user["payload"]["name"],
#     # "address" : user["payload"]["address"],
#     # "job" : user["payload"]["job"],
#     # "score" : user["payload"]["score"] for user in users
# # }
# print(users_dict)

# users_dict = {
#     "type": user["metadata"]["type"] for user in users,
#     "event_at": user["metadata"]["event_at"] for user in users,
#     "event_id": user["metadata"]["event_id"] for user in users,
#     "id": user["payload"]["id"] for user in users,
#     "name": user["payload"]["name"] for user in users,
#     "address": user["payload"]["address"] for user in users,
#     "job": user["payload"]["job"] for user in users,
#     "score": user["payload"]["score"] for user in users
# }
user_list_dict = []
for user in users:
    type = user["metadata"]["type"]
    event_at = user["metadata"]["event_at"]
    event_id = user["metadata"]["event_id"]
    id = user["payload"]["id"]
    name = user["payload"]["name"]
    address = user["payload"]["address"]
    job = user["payload"]["job"]
    score = user["payload"]["score"]
    user_dict = {
        "type" : type,
        "event_at" : event_at,
        "event_id" : event_id,
        "id" : id,
        "name" : name,
        "address" : address,
        "job" : job,
        "score" : score
    }
    user_list_dict.append(user_dict)



for i in user_list_dict:
    print(i)
    print("-"*40)
    
   


