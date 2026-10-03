class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, i: int) -> int:
        current = self.head

        for _ in range(i):
            if current is None:
                return -1
            current = current.next

        if current is None:
            return -1

        return current.val

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def remove(self, i: int) -> bool:
        if self.head is None:
            return False

        if i == 0:
            self.head = self.head.next
            return True

        current = self.head

        for _ in range(i - 1):
            if current.next is None:
                return False
            current = current.next

        if current.next is None:
            return False

        current.next = current.next.next
        return True

    def getValues(self) -> list[int]:
        values = []
        current = self.head

        while current is not None:
            values.append(current.val)
            current = current.next

        return values