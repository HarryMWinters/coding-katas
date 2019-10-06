import unittest
from solution import fibonacci as func

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    {
        "input": 0,
        "solution": 0
    },
    {
        "input": 1,
        "solution": 1
    },
    {
        "input": 3,
        "solution": 2
    },
    {
        "input": 5,
        "solution": 5
    },
    {
        "input": 12,
        "solution": 144
    },
    {
        "input": 17,
        "solution": 1597
    },
    {
        "input": 30,
        "solution": 832040
    },

    # These work but take forever.
    # {
    #     "input": 35,
    #     "solution": 9227465
    # },
    # {
    #     "input": 37,
    #     "solution": 24157817
    # },
]


class TestFibonacci(unittest.TestCase):
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
