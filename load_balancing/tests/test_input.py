from load_balancing.io import input

import os

FOLDER = os.path.dirname(os.path.abspath(__file__))

def test_input():
    usersPerTick = [1, 3, 0, 1, 0, 1]
    file = os.path.join(FOLDER, "..", "io", "input.txt")
    assert input.parse_input(file) == (4, 2, usersPerTick)