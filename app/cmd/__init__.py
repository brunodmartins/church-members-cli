import json
import logging

import click

from app.internal import service, api
from app.internal.config import CONFIG_PATH, Configuration

__gateway = api.ChurchMembersGateway()
__authentication_service = service.AuthenticationService(__gateway)
__member_service = service.ChurchMembersService(__gateway)


@click.command()
@click.option("--host", prompt="Host", help="The church members API host")
@click.option("--church-id", prompt="Church ID", help="The church ID")
def setup(host, church_id):
    try:
        Configuration.save_config({"host": host, "church_id": church_id})
        click.echo(
            click.style(f"Setup saved on {CONFIG_PATH}", fg="green"),
            err=True,
            color=True,
        )
    except Exception as e:
        click.echo(click.style(e, fg="red"), err=True, color=True)
        logging.exception("Error storing config")


@click.command()
@click.option("--user", prompt="User", help="The username")
@click.option("--password", prompt="Password", help="The password", hide_input=True)
def login(user, password):
    try:
        __authentication_service.login(user, password)
        click.echo(click.style("Login done", fg="green"), err=True, color=True)
    except Exception as e:
        click.echo(click.style(e, fg="red"), err=True, color=True)
        logging.exception("Error doing login")


@click.command("get-member")
@click.option("--member-id", prompt="Member ID", help="The member ID")
def get_member(member_id):
    try:
        token = __authentication_service.get_token()
        member = __member_service.get_member(member_id, token)
        click.echo(json.dumps(member, indent=4, sort_keys=True, ensure_ascii=False))
    except Exception as e:
        click.echo(click.style(e, fg="red"), err=True, color=True)
        logging.exception("Error getting member")
