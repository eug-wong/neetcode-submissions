class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        counter = 0
        longest = 0
        j = 0
        i = 0
        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                counter += 1
            else:
                while (True):
                    seen.remove(s[i])
                    i += 1
                    counter -= 1
                    if s[j] not in seen:
                        break
                seen.add(s[j])
                counter += 1
            print(seen)
            longest = max(counter, longest)
            j += 1
        
        return longest
