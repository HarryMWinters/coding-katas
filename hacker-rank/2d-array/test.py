import unittest
import array2D

test_data = [
    {
        "data": [[1, 1, 1, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0],
                 [1, 1, 1, 0, 0, 0],
                 [0, 0, 2, 4, 4, 0],
                 [0, 0, 0, 2, 0, 0],
                 [0, 0, 1, 2, 4, 0]],
        "answer": 19
    },
    {
        "data": [[1, 1, 1, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0],
                 [1, 1, 1, 0, 0, 0],
                 [0, 9, 2, -4, -4, 0],
                 [0, 0, 0, -2, 0, 0],
                 [0, 0, -1, -2, -4, 0]],
        "answer": 13
    },
    {
        "data": [[-9, -9, -9, 1, 1, 1],
                 [0, -9, 0, 4, 3, 2],
                 [-9, -9, -9, 1, 2, 3],
                 [0, 0, 8, 6, 6, 0],
                 [0, 0, 0, -2, 0, 0],
                 [0, 0, 1, 2, 4, 0]],
        "answer": 28
    }
]


class Test2DArrayFunctions(unittest.TestCase):

    def test__mask(self):
        expected_mask = [
            [0, 0], [0, 1], [0, 2],
            [1, 1],
            [2, 0], [2, 1], [2, 2]
        ]
        self.assertEqual(
            array2D._mask(0, 0),
            expected_mask
        )

    def test_hourGlassSum(self):
        for case in test_data:
            self.assertEqual(
                case["answer"],
                array2D.hourglassSum(case["data"])
            )


if __name__ == '__main__':
    unittest.main()
