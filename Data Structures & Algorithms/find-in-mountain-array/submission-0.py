class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        
        # Step 1: Find the index of the peak element
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            # If the current element is smaller than the next, we are going up the mountain.
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1
            # Otherwise, we are at the peak or going down.
            else:
                r = mid
        
        peak = l 
        
        # Step 2: Binary search on the ascending left half
        l, r = 0, peak
        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
                
        # Step 3: Binary search on the descending right half
        l, r = peak + 1, n - 1
        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            # Notice the logic is reversed here because the array is descending!
            elif val > target:
                l = mid + 1
            else:
                r = mid - 1
                
        # Target was not found in either half
        return -1