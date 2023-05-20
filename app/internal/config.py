import json
import os.path

HOME_FOLDER = os.path.expanduser("~")
CONFIG_FOLDER = f"{HOME_FOLDER}/.church-members"
CONFIG_PATH = f"{CONFIG_FOLDER}/config.json"


class Configuration:
    """
    Read and store system configurations on the file system
    """

    @staticmethod
    def save_config(config: dict) -> None:
        """
        Save a given configuration
        :param config: A configuration dictionary
        """
        if not os.path.exists(CONFIG_FOLDER):
            os.makedirs(CONFIG_FOLDER)
        with open(CONFIG_PATH, "w+") as f:
            f.write(json.dumps(config))

    @staticmethod
    def read_config() -> dict:
        """
        Read the configuration stored
        :return the store configuration
        """
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
