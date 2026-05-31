class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i = 0
        j = 0
        nums = []
        
        # Use 'and' to avoid Index Out Of Bounds
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        nums.extend(nums1[i:])
        nums.extend(nums2[j:])    

        n = len(nums)
        if n % 2 != 0:
            return float(nums[n // 2])
        else:
            return (nums[n // 2] + nums[(n // 2) - 1]) / 2.0