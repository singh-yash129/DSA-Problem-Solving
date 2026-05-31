class TimeMap:

    def __init__(self):
        self.time = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time:
            self.time[key].append([value, timestamp])
        else:
            self.time[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        if key in self.time:
            values = self.time[key]
            l, r = 0, len(values) - 1
            
        
            while l <= r:
                mid = (l + r) // 2
                
                if values[mid][1] <= timestamp:
                 
                    res = values[mid][0]
                  
                    l = mid + 1
                else:
                 
                    r = mid - 1
                    
        return res