class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        overlaps = set(mat[0])
        for row in mat:
            overlaps = overlaps.intersection(set(row))
        
        return min(overlaps) if overlaps else -1