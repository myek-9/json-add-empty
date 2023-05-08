"""Imports from Python Standart Library"""
import json
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()

DEV_JSON_PATH = "test_sample/template.json"
FILE_TYPES = [("json files", "*.json")]

lacking_json_path = filedialog.askopenfilename(filetypes=FILE_TYPES)
lacking_name = lacking_json_path.split("/")[-1].split(".")[0]


def update_missing_items(dev_json, not_complete_json):
    """Recursive function that updates nested json with empty str based on template - dev json"""

    for key in dev_json:
        if key not in not_complete_json:
            if isinstance(dev_json[key], dict):
                not_complete_json[key] = {}
                update_missing_items(dev_json[key], not_complete_json[key])
            else:
                not_complete_json[key] = ""
        else:
            if isinstance(dev_json[key], dict) and isinstance(not_complete_json[key], dict):
                update_missing_items(dev_json[key], not_complete_json[key])
            elif isinstance(dev_json[key], list) and isinstance(not_complete_json[key], list):
                for index, item in enumerate(dev_json[key]):
                    if isinstance(item, dict) and isinstance(not_complete_json[key][index], dict):
                        update_missing_items(
                            item, not_complete_json[key][index])


with open(DEV_JSON_PATH, encoding='utf-8') as f1, open(lacking_json_path, encoding='utf-8') as f2:
    dev_loaded = json.load(f1)
    missing_items = json.load(f2)

update_missing_items(dev_loaded, missing_items)

os.chdir(lacking_json_path.rsplit("/", 1)[0])

with open(f"{lacking_name}_updated.json", "w", encoding='utf-8') as f:
    json.dump(missing_items, f, ensure_ascii=False, indent=4)
