import unittest
from functools import cmp_to_key
from solution import Player

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    {
        "input": [
            ["amy", 100],
            ["david", 100],
            ["heraldo", 50, ],
            ["aakansha", 75],
            ["aleksa", 150],
        ],
        "solution": [
            ["aleksa", 150],
            ["amy", 100],
            ["david", 100],
            ["aakansha", 75],
            ["heraldo", 50, ],
        ]

    },
]


class TestCtciComparatorSorting(unittest.TestCase):
    def test__func(self):
        for case in test_data:
            inputArr = case["input"]
            with self.subTest(f"\ninputArr = {inputArr}\n"):
                data = []
                for name, score in inputArr:
                    player = Player(name, score)
                    data.append(player)

                result = sorted(data, key=cmp_to_key(Player.comparator))
                self.assertEqual(
                    case["solution"],
                    [[x.name, x.score] for x in result]
                )


if __name__ == '__main__':
    unittest.main()
