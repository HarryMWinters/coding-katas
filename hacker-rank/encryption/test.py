import unittest
from solution import encryption as func

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    {
        "input": "haveaniceday",
        "solution": "hae and via ecy"
    },
    {
        "input": "feedthedog",
        "solution": "fto ehg ee dd"
    },
    {
        "input": "chillout",
        "solution": "clu hlt io"
    },
]


class TestEncryption(unittest.TestCase):
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
