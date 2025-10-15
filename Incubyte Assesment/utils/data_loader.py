import json
import os

def load_json(file_name):
    """Loads JSON data from test_data folder."""
    base_path = os.path.dirname(os.path.dirname(__file__))  # go one level up
    file_path = os.path.join(base_path, "test_data", file_name)

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
