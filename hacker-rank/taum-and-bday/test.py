import unittest
from solution import taumBday as func

test_data = [
    # b: the number of black gifts
    # w: the number of white gifts
    # bc: the cost of a black gift
    # wc: the cost of a white gift
    # z: conversion cost
    {
        "input": [10, 10, 1, 1, 1],
        "solution": 20
    },
    {
        "input": [5, 9, 2, 3, 4],
        "solution": 37
    },
    {
        "input": [3, 6, 9, 1, 1],
        "solution": 12
    },
    {
        "input": [7, 7, 4, 2, 1],
        "solution": 35
    },
    {
        "input": [3, 3, 1, 9, 2],
        "solution": 12
    },
]

# b: the number of black gifts
# w: the number of white gifts
# bc: the cost of a black gift
# wc: the cost of a white gift
# z: conversion cost


class TestMarkAndToys(unittest.TestCase):
    def test__func(self):
        for case in test_data:
            b, w, bc, wc, z = case["input"]
            with self.subTest(f"\n\tb = {b}\n\tw = {w}\n\tbc = {bc}\n\twc = {wc}\n\tz = {z}\n"):
                self.assertEqual(
                    case["solution"],
                    func(b, w, bc, wc, z)
                )


if __name__ == '__main__':
    unittest.main()
