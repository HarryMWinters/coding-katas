import unittest
import bubbleSort as bs

test_data = [
    {"data": [3, 2, 1], "answer": ([1, 2, 3], 3)},
    {"data": [1, 2, 3], "answer": ([1, 2, 3], 0)}
]


class Test2DArrayFunctions(unittest.TestCase):

    def test_bubbleSortself(self):
        for case in test_data:
            self.assertEqual(
                case["answer"],
                bs.bubbleSort(case["data"])
            )


if __name__ == '__main__':
    unittest.main()
