class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        freq2 = {}
        queue = [] # elements added to freq in order
        sl = len(s1)
        sr = len(s2)

        if sl > sr:
            return False

        for i in range(sl):
            freq2[s2[i]] = freq2.get(s2[i], 0) + 1
            freq1[s1[i]] = freq1.get(s1[i], 0) + 1
            queue.append(s2[i])
        
        if freq1 == freq2:
                return True

        for i in range(sl, len(s2), 1):
            if freq1 == freq2:
                return True

            if queue[0] in freq2 and freq2[queue[0]] == 1:
                freq2.pop(queue[0])
                queue = queue[1: ]
            else:
                freq2[queue[0]] = freq2.get(queue[0], 0) - 1
                queue = queue[1: ]

            freq2[s2[i]] = freq2.get(s2[i], 0) + 1
            queue.append(s2[i])

            if freq1 == freq2:
                return True

        
        return False
