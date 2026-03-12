class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range (0,len(nums)):
            values = nums[i]
            difference = target - values 
            if values not in d :
                d[difference] = i
            else:
                current_index = i
                prev_index = d[values]
                return [ current_index,prev_index ]