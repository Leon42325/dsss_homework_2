import unittest
from math_quiz import random_number, random_operator, calculate


class TestMathGame(unittest.TestCase):

    def test_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(100):  # Test a large number of random values
            rand_num = random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # Test if operators are generated correctly
        operators_allowed = ["+", "-", "*"]
        for _ in range(100):
             operator = random_operator()
             self.assertTrue(operator in operators_allowed)

    def test_calculate(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (1, 3, '+', '1 + 3', 4),
                (6, 4, '-', '6 - 4', 2),
                (8, 1, '-', '8 - 1', 7),
                (9, 2, '*', '9 * 2', 18),
                (7, 4, '*', '7 * 4', 28)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, result = calculate(num1, num2, operator)
                self.assertEqual(problem, expected_problem, f"Problem mismatch for input {num1} {operator} {num2}")
                self.assertEqual(result, expected_answer, f"Answer mismatch for input {num1} {operator} {num2}")


if __name__ == "__main__":
    unittest.main()
