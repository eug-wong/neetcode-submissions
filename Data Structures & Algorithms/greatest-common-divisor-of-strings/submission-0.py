class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        longest = ""
        for i in range(len(str1) + 1):
            rep = str1[: i]
            if str1.replace(rep, "") == "" and str2.replace(rep, "") == "":
                longest = rep

        return longest