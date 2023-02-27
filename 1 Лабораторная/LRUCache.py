class LRUCache:

    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: str) -> str:
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return ''

    def set(self, key: str, value: str) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.pop(next(iter(self.cache)))
        self.cache[key] = value

    def rem(self, key: str) -> None:
        if key in self.cache:
            del self.cache[key]
