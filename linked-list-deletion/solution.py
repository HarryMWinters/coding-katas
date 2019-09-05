import scaffold


class MySolution(scaffold.Solution):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def toPyList(self, head):
        outList = []
        current = head
        while current:
            outList.append(current.data)
            current = current.next
        return outList

    def removeDuplicates(self, param1, param2):
        """
        Return a value that solves the challange.

        Args:
            param1: A(n) type(param1), explanation...
            price2: A(n) type(param2), explanation...
        Returns:
        A solution of type type(solution)
        Raises:
            (someTypeOf)Error: if things go wrong.
        """
        pass
