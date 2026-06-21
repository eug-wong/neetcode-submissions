class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {c: i for i, c in enumerate(order)}

        def sorting(word):
            return [order[c] for c in word]

        return words == sorted(words, key=sorting)