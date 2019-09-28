import unittest
from solution import snail


class TestSnail(unittest.TestCase):
    def test_snail0(self):
        array = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(snail(array), expected)

    def test_snail1(self):
        array = [[1, 2, 3],
                 [8, 9, 4],
                 [7, 6, 5]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEquals(snail(array), expected)

    def test_snail2(self):
        array = [[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10],
                 [11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20],
                 [21, 22, 23, 24, 25]]

        expected = [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22,
                    21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
        self.assertEquals(snail(array), expected)


if __name__ == '__main__':
    unittest.main()
