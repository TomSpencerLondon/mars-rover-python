import unittest

from src.Grid import Grid
from src.Rover import Rover


class MarsRoverTest(unittest.TestCase):
    def test_return_0_0_for_empty_command(self):
        grid = Grid()
        rover = Rover(grid)
        result = rover.execute("")
        self.assertEqual("0:0:N", result)

    def test_return_0_0_E_for_R(self):
        grid = Grid()
        rover = Rover(grid)
        result = rover.execute("R")
        self.assertEqual("0:0:E", result)

if __name__ == '__main__':
    unittest.main()
