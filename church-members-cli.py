import click

from cmd import setup, login, get_member


@click.group()
def cli():
    pass


cli.add_command(setup)
cli.add_command(login)
cli.add_command(get_member)

if __name__ == "__main__":
    cli()
