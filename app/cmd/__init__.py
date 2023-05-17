import logging

import click

from app.internal import service
from app.internal.config import save_config, CONFIG_PATH


@click.command()
@click.option("--host", prompt="Host", help="The church members API host")
@click.option("--church-id", prompt="Church ID", help="The church ID")
def setup(host, church_id):
    try:
        save_config({"host": host, "church_id": church_id})
        click.echo(f"Setup saved on {CONFIG_PATH}")
    except Exception as e:
        click.echo(click.style(e, fg="red"), err=True, color=True)
        logging.exception("Error storing config")


@click.command()
@click.option("--user", prompt="User", help="The username")
@click.option("--password", prompt="Password", help="The password", hide_input=True)
def login(user, password):
    try:
        service.login(user, password)
        click.echo("Login done")
    except Exception as e:
        click.echo(click.style(e, fg="red"), err=True, color=True)
        logging.exception("Error doing login")


@click.command("get-member")
@click.option("--member-id", prompt="Member ID", help="The member ID")
def get_member(member_id):
    try:
        service.get_member(member_id)
    except Exception as e:
        click.echo(click.style(e, fg="red"), err=True, color=True)
        logging.exception("Error getting member")
