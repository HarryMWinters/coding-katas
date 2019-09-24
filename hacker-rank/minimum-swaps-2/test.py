import unittest
from solution import minimumSwaps2 as func

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    {
        "input": [4, 3, 1, 2],
        "solution": 3
    },
    {
        "input": [2, 3, 4, 1, 5],
        "solution": 3
    },
    {
        "input": [1, 3, 5, 2, 4, 6, 7],
        "solution": 3
    },
]


class TestMinimumSwaps2(unittest.TestCase):
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
