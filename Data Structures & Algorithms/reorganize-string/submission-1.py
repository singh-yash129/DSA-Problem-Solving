from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count frequencies of each character
        count = Counter(s)
        
   
        max_heap = [[-freq, char] for char, freq in count.items()]
        heapq.heapify(max_heap)
        
        res = []
 
        prev = None
        
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            res.append(char)
            freq += 1 
            
            
            if prev and prev[0] < 0:
                heapq.heappush(max_heap, prev)
                
            prev = [freq, char]
            
        result_str = "".join(res)
        
        # If the length doesn't match, it's impossible to reorganize (e.g., "aaab")
        return result_str if len(result_str) == len(s) else ""