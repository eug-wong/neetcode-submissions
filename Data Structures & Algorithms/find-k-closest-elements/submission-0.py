class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, k
        prev = float('inf')
        res = []
        while r <= len(arr):
            dist = sum(map(lambda z: abs(z - x), arr[l: r]))
            if dist < prev:
                prev = dist
                res = arr[l: r]
            
            l, r = l + 1, r + 1

        return res
