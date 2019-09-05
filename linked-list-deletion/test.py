import unittest
import solution as s

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    {
        "input": [1, 2, 2, 3, 3, 4],
        "solution": [1, 2, 3, 4]
    },
]


class TestDeleteDuplicates(unittest.TestCase):

    def test_deleteDuplicates(self):
        for case in test_data:
            tree, head = self._makeTree(case["input"])
            tree.removeDuplicates(head)
        tree.display(head)
        self.assertEqual(
            case["solution"],
            tree.toPyList(head))

    def _makeTree(self, nodeList):
        myTree = s.MySolution()
        head = None
        for data in nodeList:
            head = myTree.insert(head, data)
        return myTree, head


if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
