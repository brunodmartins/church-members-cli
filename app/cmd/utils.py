import click


def echo_form(data: dict) -> None:
    """
    Pretty echo a formulary
    :param data: a column value dictionary
    :return:
    """
    for key in data.keys():
        click.echo(click.style(f'{key}: ', fg='blue') + data[key])
