from abc import ABC, abstractmethod
from enum import Enum


class Face(Enum):
    U = 0
    D = 1
    F = 2
    B = 3
    R = 4
    L = 5


class Color(Enum):
    WHITE = Face.U.value
    YELLOW = Face.D.value
    GREEN = Face.F.value
    BLUE = Face.B.value
    RED = Face.R.value
    ORANGE = Face.L.value


class CubeNxN(ABC):

    dimensions: int

    def get_dimensions(self):
        return self.dimensions

    def has_centers(self):
        return self.dimensions % 2 != 0

    # @abstractmethod
    # def get_supported_moves(self):
    #     """
    #     Get a list of possible moves
    #     """

    # @abstractmethod
    # def execute_move(self, move):
    #     """
    #     Execute a move
    #     """


class Cube3x3(CubeNxN):

    dimensions = 3

    def __init__(self):
        self.state = {
            "edges": {
                (Face.U, Face.B): (Face.U, Face.B),
                (Face.U, Face.R): (Face.U, Face.R),
                (Face.U, Face.F): (Face.U, Face.F),
                (Face.U, Face.L): (Face.U, Face.L),
                (Face.B, Face.L): (Face.B, Face.L),
                (Face.F, Face.L): (Face.F, Face.L),
                (Face.F, Face.R): (Face.F, Face.R),
                (Face.B, Face.R): (Face.B, Face.R),
                (Face.D, Face.F): (Face.D, Face.F),
                (Face.D, Face.R): (Face.D, Face.R),
                (Face.D, Face.B): (Face.D, Face.B),
                (Face.D, Face.L): (Face.D, Face.L),
            },
            "corners": {
                (Face.U, Face.B, Face.L): (Face.U, Face.B, Face.L),
                (Face.U, Face.B, Face.R): (Face.U, Face.B, Face.R),
                (Face.U, Face.F, Face.R): (Face.U, Face.F, Face.R),
                (Face.U, Face.F, Face.L): (Face.U, Face.F, Face.L),
                (Face.D, Face.B, Face.L): (Face.D, Face.B, Face.L),
                (Face.D, Face.B, Face.R): (Face.D, Face.B, Face.R),
                (Face.D, Face.F, Face.R): (Face.D, Face.F, Face.R),
                (Face.D, Face.F, Face.L): (Face.D, Face.F, Face.L),
            },
            "centers": {
                (Face.U,): (Face.U,),
                (Face.L,): (Face.L,),
                (Face.F,): (Face.F,),
                (Face.R,): (Face.R,),
                (Face.B,): (Face.B,),
                (Face.D,): (Face.D,),
            },
        }

    def display(self):
        chars = [color_block(item) for item in [0, 0, 0]]
        print("      {}{}{}     ".format(*chars))
        print("      {}{}{}      ".format(*chars))
        print("      {}{}{}      ".format(*chars))
        chars = [color_block(item) for item in [1, 1, 1, 2, 2, 2, 3, 3, 3]]
        print("{}{}{}{}{}{}{}{}{}".format(*chars))
        print("{}{}{}{}{}{}{}{}{}".format(*chars))
        print("{}{}{}{}{}{}{}{}{}".format(*chars))
        chars = [color_block(item) for item in [4, 4, 4]]
        print("      {}{}{}      ".format(*chars))
        print("      {}{}{}      ".format(*chars))
        print("      {}{}{}      ".format(*chars))
        chars = [color_block(item) for item in [5, 5, 5]]
        print("      {}{}{}      ".format(*chars))
        print("      {}{}{}      ".format(*chars))
        print("      {}{}{}      ".format(*chars))


BLOCK_CHARACTER = "\u2588"


class ANSIColors:
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    white = "\u001b[37m"
    orange = "\033[48;2;255;165;0m"
    black = "\u001b[30m"
    magenta = "\u001b[35m"
    cyan = "\u001b[36m"
    end = '\033[0m'


def color_block(item):
    colors = {
        Color.WHITE.value: ANSIColors.white,
        Color.YELLOW.value: ANSIColors.yellow,
        Color.GREEN.value: ANSIColors.green,
        Color.BLUE.value: ANSIColors.blue,
        Color.RED.value: ANSIColors.red,
        Color.ORANGE.value: ANSIColors.orange,
    }
    color = colors[item]
    return f"{color}{BLOCK_CHARACTER*2}{ANSIColors.end}"
