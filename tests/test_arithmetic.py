import unittest


class TestOperations(unittest.TestCase):
    def test_additions(self):
        self.assertEqual(2 + 2, 4)

    def test_subtraction(self):
        self.assertEqual(10 - 1, 9)

    def test_multiplication(self):
        self.assertEqual(2 * 3, 4)


if __name__ == "__main__":
    unittest.main()
