class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # find min and max of weights
        # do a binary search on weights to find the minimum weight capacity
        # for each mid weight, check if it fits within 4 days of shipping
        l, r = max(weights), sum(weights)
        mid = 0
        minimum = r
        while l <= r:
            mid = (l + r) // 2

            # check number of days needed
            days_needed = 1
            cargo = 0
            for w in weights:
                cargo += w
                if cargo > mid:
                    days_needed += 1
                    cargo = w
            
            # mid can decrease
            if days_needed <= days:
                minimum = min(minimum, mid)
                r = mid - 1
            elif days_needed > days:
                l = mid + 1
        
        return minimum
        