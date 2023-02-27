from LRUCache import LRUCache
cache = LRUCache(3)

cache.set("A", "Alpha")
cache.set("B", "Beta")
cache.set("C", "Gamma")
print(cache.get("A")) # "Alpha"
cache.set("D", "Delta") # Это переполнит кэш, удалив "B" из кэша, так как он был использован раньше всех остальных ключей
print(cache.get("B")) # None, так как "B" был удален из кэша из-за его переполнения
print(cache.get("A")) # "Alpha", так как мы получили его ранее и обновили его порядок
print(cache.get("C")) # "Gamma"
cache.rem("A") # Удаляем ключ "A" из кэша
print(cache.get("A")) # None, так как мы удалили ключ "A"
