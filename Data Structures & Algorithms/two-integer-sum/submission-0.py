class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        seen = {}
        nums = [3,4,5,6], target = 7

        7 - 3 is that in seen? if yes return, otherwise don't
        seen[num] = i
        '''

        num_to_index = {}
        for i in range(len(nums)):
            if target - nums[i] in num_to_index:
                return [num_to_index[target-nums[i]], i]
            
            num_to_index[nums[i]] = i