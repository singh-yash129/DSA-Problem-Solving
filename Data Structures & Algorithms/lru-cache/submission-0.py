class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # maps key -> Node

        # Dummy nodes: left = LRU, right = MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # Helper: Remove node from doubly linked list
    def _remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # Helper: Insert node at the MRU position (just before right dummy)
    def _insert(self, node: Node) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            # Update usage order: remove and re-insert at MRU
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and move to MRU
            self._remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        # Evict LRU if capacity exceeded
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]