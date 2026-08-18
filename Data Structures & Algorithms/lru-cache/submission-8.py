class Node:
    key: int | None
    val: int | None
    prev: Node | None
    next: Node | None

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        

class LRUCache:
    cap: int
    left: Node
    right: Node
    cache: Dict[int, Node]

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.cache[node.key]
        del node

    def insert(self, key: int, val: int):
        # to the right side
        node = Node(key, val)
        self.cache[key] = node

        node.next = self.right
        node.prev = self.right.prev
        node.next.prev = node
        node.prev.next = node

    def __init__(self, capacity: int):
        self.cap = capacity
        # left is LRU
        self.left, self.right = Node(None, None), Node(None, None)
        self.right.prev = self.left
        self.left.next = self.right
        self.cache = {}
        
    def get(self, key: int) -> int:
        res = self.cache.get(key, None)
        if res is None:
            return -1
        key, val = res.key, res.val
        self.remove(res)
        self.insert(key, val)
        return val
        
    def put(self, key: int, value: int) -> None:
        # replace existing, add without remove, remove and add
        node = self.cache.get(key, None)
        if node is not None:
            # replace
            self.remove(node)
            self.insert(key, value)
            return
        if len(self.cache) >= self.cap:
            self.remove(self.left.next)
        self.insert(key, value)

