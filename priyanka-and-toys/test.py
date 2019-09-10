import unittest
import solution as s

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    {
        "input": [1, 2, 3, 21, 7, 12, 14, 21],
        "solution": 4
    },
    {
        "input": [12, 15, 7, 8, 19, 24],
        "solution": 4
    }
]


class TestMarkAndToys(unittest.TestCase):
    def test__func(self):
        for case in test_data:
            A = case["input"]
            with self.subTest(f"A = {A}"):
                self.assertEqual(
                    case["solution"],
                    s.toys(A)
                )


if __name__ == '__main__':
    unittest.main()
