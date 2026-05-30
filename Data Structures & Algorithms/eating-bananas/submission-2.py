import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high # Default answer to the max possible speed

        while low <= high:
            k = (low + high) // 2
            
            # Calculate total hours needed with current eating rate 'k'
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p / k)
                
            # If Koko can finish within h hours, try a slower speed
            if total_hours <= h:
                res = min(res, k)
                high = k - 1
            # If it takes too long, Koko needs to eat faster
            else:
                low = k + 1
                
        return res