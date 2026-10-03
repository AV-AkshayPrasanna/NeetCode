class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_last(self):
        if self.size == 0:
            return None

        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0

        self.nodes = {}
        self.freq_lists = {}

    def _update(self, node):
        freq = node.freq
        self.freq_lists[freq].remove(node)

        if freq == self.min_freq and self.freq_lists[freq].size == 0:
            self.min_freq += 1

        node.freq += 1

        if node.freq not in self.freq_lists:
            self.freq_lists[node.freq] = DoublyLinkedList()

        self.freq_lists[node.freq].add(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self._update(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._update(node)
            return

        if self.size == self.capacity:
            lru = self.freq_lists[self.min_freq].remove_last()
            del self.nodes[lru.key]
            self.size -= 1

        node = Node(key, value)
        self.nodes[key] = node

        if 1 not in self.freq_lists:
            self.freq_lists[1] = DoublyLinkedList()

        self.freq_lists[1].add(node)

        self.min_freq = 1
        self.size += 1