import click
from flask.cli import FlaskGroup
from . import create_app


@click.group(cls=FlaskGroup, create_app=create_app)
def main():
    """Management script for the python_template_usage application."""


if __name__ == "__main__":  # pragma: no cover
    main()
