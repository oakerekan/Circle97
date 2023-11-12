# import libraries needed on this project
import os
import json
import csv




def load_json_files_from_folder(folder_path):
    json_data = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as f:
                json_data.append(json.load(f))

    return json_data

# Get a list of all JSON files in the folder.
folder_path_users = ("C:/Users/Olayinka Akerekan/Desktop/altschool/events/events/users/")
folder_path_cards = ("C:/Users/Olayinka Akerekan/Desktop/altschool/events/events/cards/")

# Load the json data into variables for users and cards
users = load_json_files_from_folder(folder_path_users)
cards = load_json_files_from_folder(folder_path_cards)

# Process user data
user_lists = []
for user in users:
    user_dict = {
        "type": user["metadata"]["type"],
        "event_at": user["metadata"]["event_at"],
        "event_id": user["metadata"]["event_id"],
        "id": user["payload"]["id"],
        "name": user["payload"]["name"],
        "address": user["payload"]["address"],
        "job": user["payload"]["job"],
        "score": user["payload"]["score"]
    }
    user_lists.append(user_dict)

# Process card data
card_lists = []
for card in cards:
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

# Write user data to CSV
with open('users.csv', 'w', newline='') as csv_file:
    fieldnames = user_lists[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(user_lists)

# Write card data to CSV
with open('cards.csv', 'w', newline='') as csv_file:
    fieldnames = card_lists[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(card_lists)
