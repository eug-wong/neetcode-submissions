# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        r, c = binaryMatrix.dimensions()
        best = float('inf')
        for i in range(r):
            l, r = 0, best if best != float('inf') else c - 1
            while l <= r:
                mid = (l + r) // 2
                n = binaryMatrix.get(i, mid)
                if n == 1:
                    best = mid
                    r = mid - 1
                elif n == 0:
                    l = mid + 1
                else:
                    r = mid - 1
                
        return best if best != float('inf') else -1