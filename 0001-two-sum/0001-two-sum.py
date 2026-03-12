class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range (0,len(nums)):
            values = nums[i]
            difference = target - values 
            if values not in a:
                a[difference] = i
            else:
                current_index = i
                prev_index = a[values]
                return [ current_index,prev_index ]