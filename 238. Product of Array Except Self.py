class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        answer=[1]*length
        
        pre=1
        post=1
        for i in range(length):
            answer[i]*=pre
            pre=pre*nums[i]
            answer[i]*=post
            post=post*nums[i]
        return answer
