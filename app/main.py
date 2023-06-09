import click

from app.cmd import setup, login, get_member, search_member


@click.group()
def cli():
    pass


cli.add_command(setup)
cli.add_command(login)
cli.add_command(get_member)
cli.add_command(search_member)

if __name__ == "__main__":
    cli()
