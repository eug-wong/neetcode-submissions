class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        compiled = []
        for row in matrix:
            compiled += row
        
        l, r = 0, len(compiled) - 1
        while l <= r:
            mid = (l + r) // 2
            if compiled[mid] > target:
                r = mid - 1
            elif compiled[mid] < target:
                l = mid + 1
            else:
                return True
        
        return False