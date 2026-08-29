class MedianFinder:

    def __init__(self):
        self.arr= []
        self.count=0
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        self.count+=1
        return 

    def findMedian(self) -> float:
        if self.count % 2 != 0:
            return self.arr[self.count // 2]
        return (self.arr[(self.count // 2) -1]+ self.arr[self.count // 2]) /2
        
        