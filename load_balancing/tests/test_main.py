from load_balancing import main
import os

FOLDER = os.path.dirname(os.path.abspath(__file__))

def test_main():
    file = os.path.join(FOLDER, "..", "io", "input.txt")
    var = main.main(file)
    assert var == [ [1], [2, 2], [2, 2], [1, 2, 2], [2, 2], [2], [2], [1], [1], [], 15]