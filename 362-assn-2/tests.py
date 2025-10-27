import unittest
from contrived_func import contrived_func


class TestCase(unittest.TestCase):
    def test1(self):
        contrived_func(1)

    def test2(self):
        contrived_func(10)

    def test3(self):
        contrived_func(0)

    def test4(self):
        contrived_func(3)

    def test5(self):
        contrived_func(50)

    def test6(self):
        contrived_func(25)

    def test7(self):
        contrived_func(15)

    def test8(self):
        contrived_func(39)


if __name__ == "__main__":
    unittest.main()
