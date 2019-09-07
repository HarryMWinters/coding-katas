import unittest
import solution as s

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    {
        "input": 12,
        "solution": False
    },
    {
        "input": 5,
        "solution": True
    },
    {
        "input": 7,
        "solution": True
    },
    {
        "input": 79,
        "solution": True
    },
    {
        "input": 10,
        "solution": False
    },
    {
        "input": 1,
        "solution": False
    },
    {
        "input": 2,
        "solution": True
    }
]

aux_test_data = [
    {
        "input": 100,
        "output": [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    }
]


class TestisPrime(unittest.TestCase):
    def test__isPrime(self):
        for case in test_data:
            self.assertEqual(
                case["solution"],
                s.isPrime(case["input"])
            )

    def test___extendPrimeList(self):
        for case in aux_test_data:
            testList = [2]
            s._extendPrimeList(case["input"], prime_list=testList)
            self.assertEqual(
                testList,
                case["output"]
            )
            testList = [2]


if __name__ == '__main__':
    unittest.main()
