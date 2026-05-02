class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(i-j)<= k and nums[i] == nums[j]:
                    return True
        return False            
        