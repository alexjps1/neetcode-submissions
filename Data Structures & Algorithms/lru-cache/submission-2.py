class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.order = []
        self.cap = capacity
        

    def get(self, key: int) -> int:
        res = self.cache.get(key, None)
        if res is not None:
            self.order.remove(key)
            self.order.append(key)
        return -1 if res is None else res
        
    def put(self, key: int, value: int) -> None:
        if key in self.order:
            self.order.remove(key)
            self.order.append(key)
            self.cache[key] = value
        elif len(self.order) >= self.cap:
            del self.cache[self.order[0]]
            self.order.pop(0)
            self.order.append(key)
            self.cache[key] = value
        else:
            self.order.append(key)
            self.cache[key] = value
            

        
