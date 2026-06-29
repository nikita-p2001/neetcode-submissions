class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftprod =[1]*len(nums)
        rightprod=[1]*len(nums)
        for i in range(1,len(nums)):
            leftprod[i]=leftprod[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            rightprod[i]=rightprod[i+1]*nums[i+1]
        res=[1]*len(nums)
        for i in range(len(nums)):
            res[i]=leftprod[i]*rightprod[i]
        return res
        

#[1,2,4,6]
#[1,1,2,8]
#[48,24,6,1]