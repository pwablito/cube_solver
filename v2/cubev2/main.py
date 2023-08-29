import click

from .cube import Cube3x3


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


@main.command()
def sim3():
    cube = Cube3x3()
    cube.display()


if __name__ == "__main__":
    main()
