import unittest
import solution as s

test_data = [
    {
        "input": [10, [2, 1, 3], [7, 8, 10]],
        # k, A, B
        "solution": True
    },
    {
        "input": [5, [1, 2, 2, 1], [3, 3, 3, 4]],
        # k, A, B
        "solution": False
    },
]


class TestMarkAndToys(unittest.TestCase):
    def test__func(self):
        for case in test_data:
            k, A, B = case["input"][0], case["input"][1], case["input"][2]
            self.assertTrue(
                case["solution"],
                s.twoArrays(k, A, B)
            )


if __name__ == '__main__':
    unittest.main()
