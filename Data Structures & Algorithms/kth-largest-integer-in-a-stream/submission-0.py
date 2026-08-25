class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k =k
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        arr = sorted(self.nums,reverse=True)
        return arr[self.k-1]
        
