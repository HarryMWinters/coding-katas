import unittest
from solution import countTriplets as func

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    # {
    #     "input": [2,
    #               [1, 2, 2, 4, ]],
    #     "solution": 2
    # },
    # {
    #     "input": [3,
    #               [1, 3, 9, 9, 27, 81, ]],
    #     "solution": 6
    # },
    # {
    #     "input": [5,
    #               [1, 5, 5, 25, 125, ]],
    #     "solution": 4
    # },
    # {
    #     "input": [1,
    #               [1, 2, 3, ]],
    #     "solution": 0
    # },
    # {
    #     "input": [9,
    #               [1, 7, 9, 6, 4, 12, 6, 9, 0, 18, 81, 34]],
    #     "solution": 2
    # },
    {
        "input": [2,
                  [1, 2, 1, 2, 4]],
        "solution": 3
    },
]


class TestCountTriplets(unittest.TestCase):
    def test__func(self):
        for case in test_data:
            ratio, arr = case["input"]
            with self.subTest(f"\nratio = {ratio}\narr = {arr}"):
                self.assertEqual(
                    case["solution"],
                    func(ratio, arr)
                )


if __name__ == '__main__':
    unittest.main()
