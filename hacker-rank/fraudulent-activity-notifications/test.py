import unittest
from solution import fraudulentActivityNotifications as func

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    {
        "input": [5,
                  [2, 3, 4, 2, 3, 6, 8, 4, 5, ],
                  ],
        "solution": 2
    },
    {
        "input": [4,
                  [1, 2, 3, 4, 4, ],
                  ],
        "solution": 0
    },
    {
        "input": [3,
                  [10, 20, 30, 40, 50, ],
                  ],
        "solution": 1
    },
]


class TestFraudulentActivityNotifications(unittest.TestCase):
    def test__func(self):
        for case in test_data:
            A, B = case["input"]
            with self.subTest(f"\nA = {A}\n\tB = {B}"):
                self.assertEqual(
                    case["solution"],
                    func(A, B)
                )


if __name__ == '__main__':
    unittest.main()
