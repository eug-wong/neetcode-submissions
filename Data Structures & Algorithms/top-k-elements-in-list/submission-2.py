class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hashtable[num] = hashtable.get(num, 0) + 1
        for num, frq in hashtable.items():
            freq[frq].append(num)
        
        output = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output