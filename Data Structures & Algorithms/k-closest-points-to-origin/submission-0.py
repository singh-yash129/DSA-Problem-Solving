class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = sorted(points, key=lambda x: (x[0]**2 + x[1]**2), reverse=False)
        return arr[:k]

        