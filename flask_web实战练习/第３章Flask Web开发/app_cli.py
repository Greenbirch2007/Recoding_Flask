
import click
from flask import Flask

app = Flask(__name__)

@app.cli.command()
def initdb():
    click.echo('Init the db')
