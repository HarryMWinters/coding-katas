import unittest
from solution import ctciIceCreamParlor as func

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    # {
    #     "input": [4, [1, 4, 5, 3, 2]],
    #     "solution": [1, 4]
    # },
    {
        "input": [4, [2, 2, 4, 3]],
        "solution": [1, 2]
    },
]


class TestCtciIceCreamParlor(unittest.TestCase):
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
