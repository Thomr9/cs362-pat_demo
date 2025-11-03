import unittest
import random
from credit_card_validator import credit_card_validator

class TestCase(unittest.TestCase):
    def test1(self):
        tests_to_generate = 200000
        for i in range(tests_to_generate):
            expected = True
        
            # Generate random lengths between 0-25 digits
            length = random.randint(0, 26)
            credit_card_number = ""
            for i in range(length):
                credit_card_number += str(random.randint(0,9))
            
            with self.subTest():
                result = credit_card_validator(credit_card_number)
                msg = 'Failure: {} should be {}'.format(credit_card_number, expected)
                self.assertEqual(expected, result, msg)


if __name__ == "__main__":
    unittest.main()
