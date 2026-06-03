class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand = sorted(hand)
        groups = [[hand[0]]]
        for c in hand[1: ]:
            grouped = False
            for g in groups:
                if g and g[-1] == c - 1 and len(g) < groupSize:
                    g.append(c)
                    grouped = True
                    break
            if not grouped:
                groups.append([c])
        
        for g in groups:
            if len(g) != groupSize:
                return False
        
        return True