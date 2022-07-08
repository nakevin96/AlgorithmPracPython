from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        pricemin = float('inf')
        pricesdict = {}
        for key, val in enumerate(prices):
            pricesdict[key] = val
        for i in pricesdict.values():
            pricemin = min(pricemin, i)
            result = max(result, i - pricemin)

        return result


test = Solution()
prices = [7, 1, 5, 3, 6, 4]

print(test.maxProfit(prices))
