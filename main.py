import click
import requests

__author__ = "hs3city"

@click.group()
def main():
    """
    Simple CLI for managing Club Mate and other things @ hs3city.
    """
    pass

@main.command()
@click.argument('barcode', type=click.IntRange(1000000000000, 9999999999999))
def add(query):
    """Add the product to the database"""

    amount = click.prompt('Please enter amount', type=click.IntRange(0, 40), default=1)

    if(barcode == 4029764001807):
        url = 'https://mate.at.hs3.pl/add/{}'
        response = requests.get(url.format(amount))
        click.echo(response)

@main.command()
@click.argument('barcode')
def get(barcode):
    """Return the amount of the product in the database"""
    if(barcode == 4029764001807):
        url = 'https://mate.at.hs3.pl/'
        response = requests.get(url)
        click.echo(response)

@main.command()
@click.argument('barcode')
def withdraw(barcode):
    """Withdraw one item of the product in the database"""
    if(barcode == 4029764001807):
        url = 'https://mate.at.hs3.pl/one'
        response = requests.get(url)
        click.echo(response)



if __name__ == "__main__":
    main()