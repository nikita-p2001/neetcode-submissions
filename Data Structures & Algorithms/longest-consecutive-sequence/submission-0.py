class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxi = 1
        for m in s:
            num = m - 1 
            count = 1
            while num in s:
                count+=1
                num = num -1
            maxi = max(count,maxi)
        return maxi

        