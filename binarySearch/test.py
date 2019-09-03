
import unittest
import binarySearch as bs

test_data = [
    {"data": [3, 5, 2, 1, 4, 6, 7],
     "answer": 3},
    {"data": [1],
     "answer": 0},
    {"data": [1, 2],
     "answer": 1},
    {"data": [2, 1],
     "answer": 1},
    {"data": [2, 1, 3],
     "answer": 1},
    {"data": [2, 1, 3, 4],
     "answer": 2}
]


class Test2DArrayFunctions(unittest.TestCase):

    def test_hourGlassSum(self):
        for case in test_data:
            testTree = bs.MySolution()
            root = None
            for i in case["data"]:
                root = testTree.insert(root, i)

            height = testTree.getHeight(root)
            self.assertEqual(
                case["answer"],
                height
            )


if __name__ == '__main__':
    unittest.main()
