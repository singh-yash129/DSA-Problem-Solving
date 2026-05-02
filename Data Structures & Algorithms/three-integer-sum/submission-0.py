class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() 

        def two_sum(start_idx, target):
            left, right = start_idx, len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    res.append([-target, nums[left], nums[right]])
                    left += 1
                    right -= 1
                   
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        for i in range(len(nums)):
           
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
          
            two_sum(i + 1, -nums[i])
            
        return res