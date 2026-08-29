class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. Build frequency map manually using a dictionary
        freq = {}
        for i in tasks:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        res = 0

        while any(v > 0 for v in freq.values()):
            tasks_executed = 0
            
         
            keys = list(freq.keys())
            keys.sort(key=lambda k: freq[k], reverse=True)
            
            for key in keys:
                if freq[key] > 0:
                    freq[key] -= 1
                    tasks_executed += 1
                    res += 1
                    
                    if tasks_executed == n + 1:
                        break
            
        
            if any(v > 0 for v in freq.values()):
                idle_slots = (n + 1) - tasks_executed
                if idle_slots > 0:
                    res += idle_slots

        return res