class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies=max(candies)
        res=[]
        for i in range(0,len(candies)):
            if candies[i]+extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False)

        return res

        