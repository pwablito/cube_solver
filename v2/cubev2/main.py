import click


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


if __name__ == "__main__":
    main()
