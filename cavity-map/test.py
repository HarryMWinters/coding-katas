import unittest
import cavityMap as cm

test_data = [
    {
        "data": ["1112",
                 "1912",
                 "1892",
                 "1234"],
        "answer": ["1112",
                   "1X12",
                   "18X2",
                   "1234"]
    },
    {
        "data": ["989",
                 "191",
                 "111"],
        "answer": ["989",
                   "1X1",
                   "111"]
    },
]


class TestCavityMap(unittest.TestCase):
    def test__isCavityWhenIsTrue(self):
        self.assertTrue(
            True,
            cm._isCavity(
                ['1112', '1912', '1892', '1234'], 2, 2)
        )

    def test__isCaviyWhenIsFalse(self):
        self.assertFalse(
            cm._isCavity(
                ['1112', '1912', '1892', '1234'], 2, 1
            )
        )

    def test_cavityMap(self):
        for case in test_data:
            self.assertEqual(
                case["answer"],
                cm.cavityMap(case["data"])
            )


if __name__ == '__main__':
    unittest.main()
