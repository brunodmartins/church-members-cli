import click

from internal import service
from internal.config import save_config, CONFIG_PATH


@click.command()
@click.option("--host", prompt="Host", help="The church members API host")
@click.option("--church-id", prompt="Church ID", help="The church ID")
def setup(host, church_id):
    save_config({"host": host, "church_id": church_id})
    click.echo(f"Setup saved on {CONFIG_PATH}")


@click.command()
@click.option("--user", prompt="User", help="The username")
@click.option("--password", prompt="Password", help="The password", hide_input=True)
def login(user, password):
    service.login(user, password)
    click.echo("Login done")


@click.command("get-member")
@click.option("--member-id", prompt="Member ID", help="The member ID")
def get_member(member_id):
    service.get_member(member_id)
