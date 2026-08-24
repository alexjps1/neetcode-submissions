class TimeMap:

    def __init__(self):
        self.val_store = {}
        self.ts_store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.val_store.get(key, None) is None:
            self.val_store[key] = []
        if self.ts_store.get(key, None) is None:
            self.ts_store[key] = []
        self.val_store[key].append(value)
        self.ts_store[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if self.val_store.get(key, None) is None:
            return ""
        
        ts = self.ts_store[key]
        l = 0
        r = len(ts) - 1
        while l < r:
            mid = (l + r) // 2
            if ts[mid] < timestamp:
                l = mid + 1
            else:
                r = mid
        # now l is the first ts larger than or equal to timestamp
        if ts[l] > timestamp:
            l -= 1
        if l < 0:
            return ""
        return self.val_store[key][l]
        
        
