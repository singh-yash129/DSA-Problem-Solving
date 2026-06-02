class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        i=0
        while i <= len(nums)-k:
            curr_max=nums[i]
            j=i
            for _ in range(k):
                curr_max=max(curr_max, nums[j])
                j+=1
            
            output.append(curr_max)
            i+=1
        return output

