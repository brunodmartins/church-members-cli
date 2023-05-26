import json
import logging
from datetime import datetime

import click
from rich.pretty import pprint

from app.cmd import utils
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
@click.option('--format-type',
              type=click.Choice(['json', 'text'], case_sensitive=False))
def get_member(member_id, format_type):
    try:
        token = __authentication_service.get_token()
        member = __member_service.get_member(member_id, token)
        if format_type == "text":
            person = member["person"]
            form = {
                "Nome": person["fullName"],
                'Dt. Nascimento': datetime.strptime(person["birthDate"], "%Y-%m-%dT%H:%M:%SZ").strftime("%d/%m/%Y")
            }
            if "contact" in person:
                if "cellphone" in person["contact"]:
                    form['Celular'] = person["contact"]["cellphone"]
                if "phone" in person["contact"]:
                    form['Telefone'] = person["contact"]["phone"]
                    click.echo(click.style('Telefone: ', fg='blue') + person["contact"]["phone"])
                if "email" in person["contact"]:
                    form['Email'] = person["contact"]["email"]
            utils.echo_form(form)
        else:
            pprint(member, indent_guides=False)
    except Exception as e:
        click.echo(click.style(e, fg="red"), err=True, color=True)
        logging.exception("Error getting member")


@click.command("search-member")
@click.option("--name", prompt="Name", help="The member name")
@click.option("--select", is_flag=True)
def search_member(name, select):
    try:
        token = __authentication_service.get_token()
        result = __member_service.search_member(name, token)
        if select:
            index = 1
            for member in result:
                member_name = member["person"]["fullName"]
                click.echo(f"{index}) {member_name}")
                index = index + 1
            choice = click.prompt('Select a member', type=int)
            choice = choice - 1
            if choice > len(result) or choice < 0:
                raise Exception("Invalid option")
            member = __member_service.get_member(result[choice]["id"], token)
            click.echo(json.dumps(member, indent=4, sort_keys=True, ensure_ascii=False))
        else:
            pprint(result, expand_all=True, indent_guides=False)
    except Exception as e:
        click.echo(click.style(e, fg="red"), err=True, color=True)
        logging.exception("Error searching member")
