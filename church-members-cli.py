import click

from cmd import setup


@click.group()
def cli():
    pass


cli.add_command(setup)

if __name__ == "__main__":
    cli()
