import unittest
from solution import sherlockAndAnagrams as func

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    {
        "input": "abba",
        "solution": 4
    },
    {
        "input": "abcd",
        "solution": 0
    },
    {
        "input": "ifailuhkqq",
        "solution": 3
    },
    {
        "input": "kkkk",
        "solution": 10
    },
    {
        "input": "cdcd",
        "solution": 5
    },
    # {
    #     "input":
    #     "solution":
    # },
]


class TestSherlockAndAnagrams(unittest.TestCase):
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
