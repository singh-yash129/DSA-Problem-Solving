class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} 

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
   
        self.cache[key][1] += 1
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.cache:
            self.cache[key][0] = value
            self.cache[key][1] += 1
            return

     
        if len(self.cache) >= self.capacity:
         
            lfu_key = min(self.cache, key=lambda k: self.cache[k][1])
            del self.cache[lfu_key]

  
        self.cache[key] = [value, 1]