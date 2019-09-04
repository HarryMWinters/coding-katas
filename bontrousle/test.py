import unittest
import bonetrousle as b

test_data_possible = [
    # TargetValue, MaxValue, LenValues
    {
        "input": [12, 8, 3],
        "answer": []
    },
    {
        "input": [9, 10, 2],
        "answer": []
    },
    {
        "input": [9, 10, 2],
        "answer": []
    },
    {
        "input": [15, 25, 3],
        "answer": []
    },
    {
        "input": [12, 6, 3],
        "answer": []
    },
    {
        "input": [51, 18, 6],
        "answer": []
    },
    {
        "input": [38, 10, 7],
        "answer": []
    },
    {
        "input": [2, 3, 1],
        "answer": []
    },
    {
        "input": [125, 16, 14],
        "answer": []
    },
    {
        "input": [77, 18, 7],
        "answer": []
    },
    {
        "input": [3, 3, 1],
        "answer": []
    },
    {
        "input": [124, 19, 11],
        "answer": []
    },
    {
        "input": [3, 2, 2],
        "answer": []
    },
    {
        "input": [50, 16, 7],
        "answer": []
    },
    {
        "input": [122, 16, 13],
        "answer": []
    },
    {
        "input": [73, 19, 6],
        "answer": []
    },
    {
        "input": [7, 14, 1],
        "answer": []
    },
    {
        "input": [6, 3, 3],
        "answer": []
    },
    {
        "input": [13, 7, 4],
        "answer": []
    },
    {
        "input": [59, 13, 7],
        "answer": []
    },
    {
        "input": [31, 8, 7],
        "answer": []
    },
    {
        "input": [22, 7, 6],
        "answer": []
    },
    {
        "input": [22, 7, 6],
        "answer": []
    },
    {
        "input": [26, 7, 6],
        "answer": []

    },
    {
        "input": [39, 15, 3],
        "answer": []
    },
    {
        "input": [95, 20, 10],
        "answer": []
    },
    {
        "input": [25, 10, 5],
        "answer": []
    },
    {
        "input": [5, 20, 1],
        "answer": []
    },
    {
        "input": [1, 20, 1]
    },
    {
        "input": [1, 2, 1]
    },
    {
        "input": [154, 20, 10]
    },
    {
        "input": [56, 20, 10]
    },
    {
        "input": [155, 20, 10]
    }


]

test_data_impossible = [
    {
        "input": [156, 20, 10]
    },
    {
        "input": [21, 20, 1]
    },
    {
        "input": [2, 1, 1],
        "answer": []
    },
    {
        "input": [10, 3, 3],
        "answer": [-1]
    },
    {
        "input": [172, 17, 9],
        "answer": [-1]
    },
    {
        "input": [69, 9, 6, ],
        "answer": [-1]
    },
    {
        "input": [1000000000000000000, 20, 10],
        "answer": [-1]
    },
    {
        "input": [1000000000000000000, 1, 1],
        "answer": [-1]
    },
    {
        "input": [1000000000000000000, 20, 19],
        "answer": [-1]
    },
    {
        "input": [1000000000000000000, 20, 20],
        "answer": [-1]
    },
    {
        "input": [2, 1, 1],
        "answer": [-1]
    },
    {
        "input": [54, 20, 10]
    }
]


class TestCavityMap(unittest.TestCase):

    def test_solvableCases(self):
        for case in test_data_possible:
            self.assertEqual(
                case["input"][2],
                len(b.bonetrousle(case["input"][0],
                                  case["input"][1],
                                  case["input"][2]))
            )
            self.assertEqual(
                case["input"][0],
                sum(b.bonetrousle(case["input"][0],
                                  case["input"][1],
                                  case["input"][2])
                    )
            )

    def test_unsolvableCase(self):
        for case in test_data_impossible:
            self.assertEqual(
                [-1],
                b.bonetrousle(case["input"][0],
                              case["input"][1],
                              case["input"][2])
            )


if __name__ == '__main__':
    unittest.main()
