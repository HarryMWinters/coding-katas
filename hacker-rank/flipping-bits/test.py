import unittest
from solution import flippingBits as func

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    {
        "input": 2147483647,
        "solution": 2147483648
    },
    {
        "input": 1,
        "solution": 4294967294,
    },
    {
        "input": 0,
        "solution": 4294967295,
    },
]


class TestFlippingBits(unittest.TestCase):
    def test__func(self):
        for case in test_data:
            A = case["input"]
            with self.subTest(f"\nA = {A}\n"):
                self.assertEqual(
                    case["solution"],
                    func(A)
                )


if __name__ == '__main__':
    unittest.main()
