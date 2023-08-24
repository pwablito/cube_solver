from abc import ABC, abstractmethod


class NxNCube(ABC):

    dimensions: int

    def get_dimensions(self):
        return self.dimensions

    @abstractmethod
    def get_supported_moves(self):
        """
        Get a list of possible moves
        """

    @abstractmethod
    def execute_move(self, move):
        """
        Execute a move
        """
