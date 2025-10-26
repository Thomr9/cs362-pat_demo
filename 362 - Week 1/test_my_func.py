import unittest
from my_file import my_func

class TestFunc(unittest.TestCase):
    def test_my_func_true(self):
        self.assertTrue(my_func(True))

    def test_my_func_false(self):
        self.assertFalse(my_func(False))

    def test_my_func_failure(self):
        self.assertFalse(my_func(False))

if __name__ == '__main__':
    unittest.main()