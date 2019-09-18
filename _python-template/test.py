import unittest
import solution.%%CAMELCASE_NAME%% as func

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    {
        "input": [None, None],
        "solution": None
    },
]


class Test%%PASCAL_NAME%%(unittest.TestCase):
    def test__func(self):
        for case in test_data:
            A, B = case["input"]
            with self.subTest(f"\n\A = {A}\n\tB = {B}"):
                self.assertEqual(
                    case["solution"],
                    func(A, B)
                )


if __name__ == '__main__':
    unittest.main()
