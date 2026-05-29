class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target in matrix[0]:
            return True
        if target > matrix[-1][-1]:
            return False
            
        i = 1
        while i < len(matrix):
            if matrix[i][-1] < target:
                i += 1
            else:
                break
                

        if i < len(matrix) and target in matrix[i]:
            return True
            
        return False