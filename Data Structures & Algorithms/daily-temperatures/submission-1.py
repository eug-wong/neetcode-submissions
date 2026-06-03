class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        stack =  (38, 1) 
                        (36, 3)
        res = [1, 0, 1, 0, 0, 0, 0]
        '''

        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
                if not stack:
                    stack.append([temp, i])
                    continue

                while stack and stack[-1][0] < temp:
                    popped = stack.pop()
                    res[popped[1]] = i - popped[1]

                stack.append([temp, i])

        
        return res