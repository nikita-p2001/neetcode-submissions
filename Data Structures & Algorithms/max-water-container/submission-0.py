class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        maxi=0
        while l < r:
            water = min(heights[l],heights[r])*(r-l)
            if heights[r]>=heights[l]:
                l+=1
            else:
                r-=1
            maxi=max(water,maxi)
        return maxi

        