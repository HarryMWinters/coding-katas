import unittest
import solution as s

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    {
        "input": None,
        "solution": None
    },
]


class TestMarkAndToys(unittest.TestCase):
    def test__func(self):
        for case in test_data:
            self.assertTrue(
                case["solution"],
                s.func(case["input"])
            )


if __name__ == '__main__':
    unittest.main()
