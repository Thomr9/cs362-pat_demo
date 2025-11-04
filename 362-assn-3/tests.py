import unittest
import random
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    def test1(self):
        tests_to_generate = 800000
        for _ in range(tests_to_generate):
            credit_card_number = ""
            odds = random.randint(0, 3)

            # Visa prefix
            if odds == 1:
                credit_card_number += str(random.randint(3, 5))
            # Mastercard prefix
            if odds == 2:
                if random.choice([True, False]):
                    prefix = str(random.randint(50, 56))
                else:
                    prefix = str(random.randint(2220, 2721))
                credit_card_number += prefix
            # AMEX prefix
            if odds == 3:
                credit_card_number += random.choice(
                    ["33", "34", "35", "36", "37", "38"])
            # Generate random lengths between 0-18 digits
            length = random.randint(0, 18)

            for _ in range(length):
                credit_card_number += str(random.randint(0, 9))
            credit_card_validator(credit_card_number)


if __name__ == "__main__":
    unittest.main()
