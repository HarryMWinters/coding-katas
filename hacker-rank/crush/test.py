import unittest
from solution import arrayManipulation as func

test_data = [
    {
        "input": [10,
                  [
                      [1, 10, 1],
                      [4, 5, 1],
                  ]
                  ],
        "solution": 2
    },
    {
        "input": [10,
                  [
                      [1, 3, 1],
                      [4, 10, 1],
                      [6, 8, 1]
                  ]
                  ],
        "solution": 2
    },
    {
        "input": [5,
                  [
                      [1, 3, 1],
                      [3, 5, 1],
                  ]
                  ],
        "solution": 2
    },
    {
        "input": [5,
                  [
                      [3, 5, 1],
                      [1, 3, 1],
                  ]
                  ],
        "solution": 2
    },
    {
        "input": [10,
                  [
                      [1, 3, 1],
                      [5, 5, 5],
                      [6, 9, 1],
                  ]
                  ],
        "solution": 5
    },
    {
        "input": [5,
                  [
                      [1, 2, 1],
                      [2, 5, 1],
                      [3, 4, 1]
                  ]
                  ],
        "solution": 2
    },
    {
        "input": [10,
                  [
                      [1, 5, 3],
                      [4, 8, 7],
                      [6, 9, 1],
                  ]
                  ],
        "solution": 10
    },
    {
        "input": [10,
                  [
                      [2, 6, 8],
                      [3, 5, 7],
                      [1, 8, 1],
                      [5, 9, 15],
                  ]
                  ],
        "solution": 31
    },
    {
        "input": [5,
                  [
                      [1, 2, 100],
                      [2, 5, 100],
                      [3, 4, 100]
                  ]
                  ],
        "solution": 200
    },

]


class TestCrush(unittest.TestCase):
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
