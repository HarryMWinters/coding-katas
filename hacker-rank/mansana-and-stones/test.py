import unittest
import solution as s

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    {
        "input": [3, 1, 2],
        "solution": [2, 3, 4]
    },
    {
        "input": [4, 10, 100],
        "solution": [30, 120, 210, 300]
    },
    {
        "input": [5, 0, 0],
        "solution": [0]
    }
]


class TestMarkAndToys(unittest.TestCase):
    def test__stones(self):
        for case in test_data:
            numStones, A, B = case["input"][0], case["input"][1], case["input"][2]
            with self.subTest(f"\n\tnumStones = {numStones}\n\tdiffA = {A}\n\tdiffB = {B}\n"):
                self.assertEqual(
                    set(case["solution"]),
                    set(s.stones(numStones, A, B))
                )


if __name__ == '__main__':
    unittest.main()
