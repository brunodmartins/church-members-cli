import json
import os.path

HOME_FOLDER = os.path.expanduser("~")
CONFIG_FOLDER = f"{HOME_FOLDER}/.church-members"
CONFIG_PATH = f"{CONFIG_FOLDER}/config.json"


def save_config(config):
    if not os.path.exists(CONFIG_FOLDER):
        os.makedirs(CONFIG_FOLDER)
    with open(CONFIG_PATH, "w+") as f:
        f.write(json.dumps(config))
