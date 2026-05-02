class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        # You can call this with 4, 5, 6, etc.
        return self.kSum(nums, target, 4, 0)

    def kSum(self, nums: List[int], target: int, k: int, start: int) -> List[List[int]]:
        res = []
        
        # Optimization: if we don't have enough numbers left
        if start == len(nums):
            return res
        
        # Base Case: When k = 2, use two pointers to find all pairs
        if k == 2:
            return self.twoSum(nums, target, start)

        for i in range(start, len(nums)):
            # Skip duplicates for the current position
            if i > start and nums[i] == nums[i - 1]:
                continue
            
            # Recursively find (k-1) sums
            for subset in self.kSum(nums, target - nums[i], k - 1, i + 1):
                res.append([nums[i]] + subset)
        
        return res

    def twoSum(self, nums: List[int], target: int, start: int) -> List[List[int]]:
        res = []
        left, right = start, len(nums) - 1
        
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip duplicates for the two-pointer base case
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
        return res