class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sorted_counts = sorted(counts.items(), key=lambda x: x[1])
        res = []
        for k, _ in sorted_counts[-k: ]:
            res.append(k)
        
        return res