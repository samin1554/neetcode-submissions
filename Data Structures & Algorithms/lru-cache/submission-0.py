class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # move node right after head (MRU position)
    def add_front(self, node):
        first = self.head.next

        node.next = first
        node.prev = self.head

        self.head.next = node
        first.prev = node

    # remove node from linked list
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # move to front (most recently used)
        self.remove(node)
        self.add_front(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            # refresh position
            self.remove(node)
            self.add_front(node)

        else:
            node = Node(key, value)
            self.cache[key] = node
            self.add_front(node)

            # evict LRU if over capacity
            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]
        
