import logging

from app.internal.config import CONFIG_FOLDER

logging.basicConfig(
    filename=f"{CONFIG_FOLDER}/church-members-cli.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
