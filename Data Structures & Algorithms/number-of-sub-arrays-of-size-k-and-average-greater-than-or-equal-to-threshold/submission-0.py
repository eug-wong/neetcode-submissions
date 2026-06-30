class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        for r in range(k, len(arr) + 1):
            if sum(arr[r - k: r]) / k >= threshold:
                res += 1
        
        return res