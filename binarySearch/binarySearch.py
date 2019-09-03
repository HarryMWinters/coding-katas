from scaffold import Solution


class MySolution(Solution):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def getHeight(self, root):
        """
        Recursivly navigate a binary tree to find longest root to leaf route (aka the tree's height.)
        Args:
            root: A pointer to the root of a binary tree (constructed via the Solution class in scaffold.py)
        Returns:
            An integer corrosponding to the trees height.
        Raises:
            AttributeError: if root is not a Node or contains Nodes pointing to non-Node or non-None objects.
         """
        if root is None:
            return -1
            # Since terminal nodes don't add an edge
        else:
            return max(
                [self.getHeight(root.right) + 1,
                 self.getHeight(root.left) + 1])
