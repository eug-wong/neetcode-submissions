from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hashmap[key]
        # do binary search to find nearest time and return key at that time
        # upper bound is timestamp, lower bound is 1
        if not arr:
            return ""

        # target is timestamp
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] > timestamp:
                r = mid - 1
            elif arr[mid][0] < timestamp:
                l = mid + 1
            else:
                return arr[mid][1]
            
        print(arr, mid)
        # arr[mid][1] if arr[mid][0] <= timestamp else (arr[mid - 1][1] if arr[mid - 1][0] <= timestamp)
        if arr[mid][0] <= timestamp:
            return arr[mid][1]
        elif arr[mid - 1][0] <= timestamp:
            return arr[mid - 1][1]
        else:
            return ""
        
        # return arr[mid][1] if arr[mid][0] <= timestamp else (arr[mid - 1][1] if arr[mid - 1][0] <= timestamp)

        
