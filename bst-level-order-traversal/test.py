import unittest
import bstLevelOrderTraversal as s

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    {
        "input": [3, 5, 4, 7, 2, 1],
        "solution": [3, 2, 5, 1, 4, 7]
    },
]


class TestBSTLevelOrderTraversal(unittest.TestCase):

    def test__levelOrderSearch(self):
        for case in test_data:
            tree, root = self._makeTree(case["input"])
        self.assertEqual(
            case["solution"],
            tree.levelOrder(root))

    def _makeTree(self, nodeList):
        myTree = s.myTree()
        root = None
        for data in nodeList:
            root = myTree.insert(root, data)
        return myTree, root


if __name__ == '__main__':
    unittest.main()
