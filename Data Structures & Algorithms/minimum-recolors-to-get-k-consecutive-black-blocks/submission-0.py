class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        replaces = len(blocks)
        for r in range(k, len(blocks) + 1):
            counts = Counter(blocks[r - k: r])
            replaces = min(replaces, counts["W"])


        return replaces