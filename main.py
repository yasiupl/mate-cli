#!/bin/python3

import click
import requests

__author__ = "hs3city"

"""EAN Barcode of Club Mate"""
mate_barcode = 4029764001807

@click.group()
def main():
	"""
	Simple CLI using EAN Barcodes for managing Club Mate and (soon) other things @ hs3city.
	"""
	pass

@main.command()
@click.argument('barcode', type=click.IntRange(1000000000000, 9999999999999))
def add(barcode):
	"""Add the product to the database"""

	amount = click.prompt('Please enter the amount', type=click.IntRange(0, 40), default=1)
	
	if(barcode == mate_barcode):
		url = 'https://mate.at.hs3.pl/add/{}'.format(amount)
		response = requests.get(url)
		click.echo(response.text)

@main.command()
@click.argument('barcode', type=click.IntRange(1000000000000, 9999999999999))
def withdraw(barcode):
	"""Withdraw one item of the product in the database"""

	if(barcode == mate_barcode):
		url = 'https://mate.at.hs3.pl/one'
		response = requests.get(url)
		click.echo(response.text)

@main.command()
@click.argument('barcode', type=click.IntRange(1000000000000, 9999999999999))
def get(barcode):
	"""Return the information about the product in the database"""

	if(barcode == mate_barcode):
		url = 'https://mate.at.hs3.pl/'
		response = requests.get(url)
		click.echo(response.text)

if __name__ == "__main__":
	main()