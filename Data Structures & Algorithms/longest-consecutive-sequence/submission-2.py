class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxi = 0
        for m in s:
            
            if m-1 not in s:
                length =0
                while m+length in s:
                    length+=1
                maxi = max(maxi,length)
        return maxi
        
        