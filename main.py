from config import *
from worlds import TestWorld


if __name__ == '__main__':

    world = TestWorld()
    world.setup()

    world.run_tests()


