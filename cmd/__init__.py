import click

from internal.config import save_config, CONFIG_PATH


@click.command()
@click.option("--host", prompt="Host", help="The church members API host")
@click.option("--church-id", prompt="Church ID", help="The church ID")
def setup(host, church_id):
    save_config({"host": host, "church_id": church_id})
    click.echo(f"Setup saved on {CONFIG_PATH}")
