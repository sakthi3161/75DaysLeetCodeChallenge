class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        j = len(nums) - 1
        answer = [1] * len(nums)
        for i in range(len(nums)):
            answer[i] *= pre
            answer[j] *= post
            pre *= nums[i]
            post *= nums[j]
            j = j - 1
        return answer
        