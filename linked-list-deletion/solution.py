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

    def removeDuplicates(self, head):
        """
        Return None. Remove nodes with duplicate data from 
        the linked list whose head is the parameter head.

        Args:
            head: The node at the head of the linked list to be check.
        Returns:
            Reference to head of list, a Node object.
        Raises:
            (someTypeOf)Error: if things go wrong.
        """
        originalHead = head
        while head and head.next:
            if head.data == head.next.data:
                head.next = head.next.next
            else:
                head = head.next
        return originalHead
