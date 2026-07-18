class Solution:
    def maxScore(self, points: List[int], k: int) -> int:
        pointsLength = len(points)
        left, right = pointsLength - k, pointsLength - 1
        res = sum(points[left:right+1])
        currSum = sum(points[left:right+1])

        while right != k-1:
            currSum -= points[left]
            left = left + 1 if left+1 < len(points) else 0

            right = right + 1 if right+1 < len(points) else 0
            currSum += points[right]

            res = max(res, currSum)

        # currSum = currSum - points[left] + points[right]
        return max(res, currSum)