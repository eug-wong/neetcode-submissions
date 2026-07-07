class Solution:
    def calculate(self, s: str) -> int:
        equation = [""]
        i = 0
        while i < len(s):
            if s[i] not in ["+", "*", "-", "/"]:
                equation[-1] = equation[-1] + s[i]
            else:
                equation.append(s[i])
                equation.append("")
            i += 1
        
        if len(equation) == 1:
            return int(equation[0])

        # mults and divs first
        res = []
        i = 0
        while i < len(equation):
            if equation[i] in ["+", "-"]:
                res.append(equation[i])
            elif equation[i] in ["*", "/"]:
                if equation[i] == "*":
                    res.append(int(res.pop()) * int(equation[i + 1]))
                if equation[i] == "/":
                    res.append(int(res.pop()) // int(equation[i + 1]))
                i += 1
            else:
                res.append(equation[i])
            i += 1

        i = 0
        res2 = []
        while i < len(res):
            if res[i] in ["+", "-"]:
                if res[i] == "+":
                    res2.append(int(res2.pop()) + int(res[i + 1]))
                if res[i] == "-":
                    res2.append(int(res2.pop()) - int(res[i + 1]))
                i += 1
            else:
                res2.append(res[i])
            i += 1

        return res2[0]