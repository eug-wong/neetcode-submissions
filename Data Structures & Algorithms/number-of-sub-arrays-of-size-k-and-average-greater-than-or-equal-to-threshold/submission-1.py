class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        cur = sum(arr[: k])
        r = k
        if cur / k >= threshold:
                res += 1

        while r < len(arr):
            cur += arr[r]
            cur -= arr[r - k]
            if cur / k >= threshold:
                res += 1
                
            r += 1
        
        return res