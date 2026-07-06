class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        dupes = set(nums1) & set(nums2)
        res1 = set()
        for n in nums1:
            if n not in dupes:
                res1.add(n)
        
        res2 = set()
        for n in nums2:
            if n not in dupes:
                res2.add(n)

        return [list(res1), list(res2)]