class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_={}
        for i in nums:
            if i in dict_:
                dict_[i]+=1
            else:
                dict_[i]=1
        


        for i, j in dict_.items():
            if j > 1:
                return True
        return False