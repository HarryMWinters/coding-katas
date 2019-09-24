import unittest
from solution import alternatingCharacters as func

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    {
        "input": "AAAA",
        "solution": 3
    },
    {
        "input": "BBBBB",
        "solution": 4
    },
    {
        "input": "ABABABAB",
        "solution": 0
    },
    {
        "input": "BABABA",
        "solution": 0
    },
    {
        "input": "AAABBB",
        "solution": 4
    },
    {
        "input": "AAABAAA",
        "solution": 4
    }
]


class TestAlternatingCharacters(unittest.TestCase):
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
