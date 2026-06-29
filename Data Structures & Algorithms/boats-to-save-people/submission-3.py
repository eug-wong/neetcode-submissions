class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        # [1, 2, 4, 5]
        # [1, 2, 2, 3, 3]
        while l <= r:
            cur = people[r] + people[l]
            if cur <= limit:
                l += 1
            
            boats += 1
            r -= 1
        
        return boats

                