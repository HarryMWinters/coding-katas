import unittest
import markAndToys as m

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    {
        "input": {
            "moneyAvailable": 50,
            "priceList": [1, 12, 5, 111, 200, 1000, 10]
        },
        "solution": 4
    },
    {
        "input": {
            "moneyAvailable": 7,
            "priceList": [1, 2, 3, 4]
        },
        "solution": 4
    },
    {
        "input": {
            "moneyAvailable": 15,
            "priceList": [3, 7, 2, 9, 4]
        },
        "solution": 4
    }
]


class TestMarkAndToys(unittest.TestCase):
    def test__maximumToys(self):
        for case in test_data:
            self.assertTrue(
                case["solution"],
                m.maximumToys(
                    case["input"]["moneyAvailable"],
                    case["input"]["priceList"]
                )
            )


if __name__ == '__main__':
    unittest.main()
