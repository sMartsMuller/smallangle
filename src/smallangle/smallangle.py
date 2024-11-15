import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of values.",
    show_default=True,
)
def sin(number):
    """Gives a number of angles equally spaced out between 0 
    and 2pi and their sine values.

    Args:
        number (int): Number of values.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of values.",
    show_default=True,
)
def tan(number):
    """Gives a number of angles equally spaced out between 0 and 2pi 
    and their tangent values.

    Args:
        number (int): Number of values.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    sin(10)