import click
from dataclasses import dataclass


@dataclass
class Context:
    start_state: CubeState = None


@click.group()
@click.option(
    "-v",
    "--verbose",
    count=True,
)
@click.pass_context
def main(ctx, verbose):
    """
    Cube v2 Interface
    """
    pass
