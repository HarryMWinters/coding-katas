import scaffold


class myTree(scaffold.Solution):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def levelOrder(self, root):
        """
        A list of the data in each node in the order of a level order
        traversal.

        Args:
            root: The root node of the BST to be traversed.
        Returns:
            A list of int's from node data.
        Raises:
            (someTypeOf)Error: if things go wrong.
        """
        levelDict = {}
        self._traverseTree(root, 0, levelDict)
        outList = []
        levels = [i for i in levelDict.keys()]
        levels.sort()
        for level in levels:
            outList.extend(levelDict[level])
        return outList

    def _traverseTree(self, node, orderLevel, levelDict):
        if node is None:
            return

        if levelDict.get(orderLevel):
            levelDict[orderLevel].append(node.data)
        else:
            levelDict[orderLevel] = [node.data]
        self._traverseTree(node.left, orderLevel + 1, levelDict)
        self._traverseTree(node.right, orderLevel + 1, levelDict)
