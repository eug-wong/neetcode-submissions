class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))]
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        
        for item in freq.items():
            buckets[item[1] - 1].append(item[0])
        
        res = []
        i = len(nums) - 1
        while len(res) != k and i > -1:
            if buckets[i]:
                res += buckets[i]
            i -= 1
        
        return res