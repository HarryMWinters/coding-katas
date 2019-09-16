import unittest
import solution.func as func

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
            A, B, C = case["input"][0], case["input"][1], case["input"][2]
            with self.subTest(f"\n\A = {A}\n\tB = {B}\n\tC = {C}\n"):
                self.assertEqual(
                    case["solution"],
                    func(A, B, C)
                )


if __name__ == '__main__':
    unittest.main()
