import unittest
from solution import nextBiggestNumberWSameDigits as func

test_data = [
    {
        "input": 12,
        "solution": 21
    },
    {
        "input": 513,
        "solution": 531
    },
    {
        "input": 2017,
        "solution": 2071
    },
    {
        "input": 9,
        "solution": -1
    },
    {
        "input": 111,
        "solution": -1
    },
    {
        "input": 531,
        "solution": -1
    },
    {
        "input": 1234567908,
        "solution": 1234567980
    },
    {
        "input": 1234567098,
        "solution": 1234567809
    },
    {
        "input": 414,
        "solution": 441
    },
    {
        "input": 144,
        "solution": 414
    },
    {
        "input":    4072969796,
        "solution": 4072969967
    },
    {
        "input":    2291,
        "solution": 2912
    },
    {
        "input":    8987,
        "solution": 9788
    },


]


class TestNextBiggestNumberWSameDigits(unittest.TestCase):
    def test__func(self):
        for case in test_data:
            initial = case["input"]
            with self.subTest(f"\nA = {initial}\n"):
                self.assertEqual(
                    case["solution"],
                    func(initial)
                )


if __name__ == '__main__':
    unittest.main()
