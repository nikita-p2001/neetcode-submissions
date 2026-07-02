class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prefarr =[0]*len(prices)
        maxi=0
        for i in range(len(prices)-2,-1,-1):
            maxi = max(maxi,prices[i])
            prefarr[i]=maxi
        newmaxi=0
        for i in range(len(prices)):
            prof=0
            if prefarr[i]>=prices[i]:
                prof=prefarr[i]-prices[i]
                newmaxi=max(newmaxi,prof)
        return newmaxi
        


                    


