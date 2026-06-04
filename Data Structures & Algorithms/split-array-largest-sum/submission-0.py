class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        memo = {}
        
        # i is our current starting index in the array
        # partitions_left is how many subarrays we still need to form
        def expand_and_split(i: int, partitions_left: int) -> int:
            # Base Case 1: If we reached the end of the array and used all splits
            if i == len(nums) and partitions_left == 0:
                return 0
            # Base Case 2: Out of bounds or invalid split count
            if i == len(nums) or partitions_left == 0:
                return float('inf')
            
            # If we already calculated this state, return it (Memoization)
            if (i, partitions_left) in memo:
                return memo[(i, partitions_left)]
            
            min_largest_sum = float('inf')
            current_subarray_sum = 0
            
            # Here is your approach: We expand the current group to the right,
            # adding elements one by one (right, right of right, etc.)
            for j in range(i, len(nums)):
                current_subarray_sum += nums[j]
                
                # Find the largest sum for the remaining part of the array
                remaining_max = expand_and_split(j + 1, partitions_left - 1)
                
                # The largest sum for this specific configuration
                largest_sum_here = max(current_subarray_sum, remaining_max)
                
                # We want to minimize this largest sum
                min_largest_sum = min(min_largest_sum, largest_sum_here)
                
            memo[(i, partitions_left)] = min_largest_sum
            return min_largest_sum

        return expand_and_split(0, k)