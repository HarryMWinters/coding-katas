import unittest
from solution import acmTeam as func

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    {
        "input": [
            "10101",
            "11100",
            "11010",
            "00101"
        ],
        # [Maximum topics, number of combinations with maximum]
        "solution": [5, 2]

    },
    {
        "input": [
            "11101",
            "10101",
            "11001",
            "10111",
            "10000",
            "01110"
        ],
        "solution": [5, 6]
    },
    {
        "input": [
            "00000",
            "00000",
        ],
        "solution": [0, 1]
    },
    {
        "input": [line.strip() for line in open("test-data.txt")],
        "solution": [97, 5]
    }

]


class TestMarkAndToys(unittest.TestCase):
    def test__func(self):
        for case in test_data:
            A = case["input"]
            with self.subTest(f"A = {A}"):
                self.assertEqual(
                    case["solution"],
                    func(A))


if __name__ == '__main__':
    unittest.main()
