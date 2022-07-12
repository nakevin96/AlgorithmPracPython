# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = 10000
#         profit = 0
#         for price in prices:
#             min_price = min(min_price, price)
#             profit = max(profit, price - min_price)
#
#         return profit

# 처음 작성한 코드,
# O(n^2)이라 time limit초과..
# def max_profit(prices):
#     profit = []
#     for idx in range(len(prices)-1):
#         tmp = max(prices[idx+1:]) - prices[idx]
#         if tmp < 0:
#             profit.append(0)
#         else:
#             profit.append(tmp)
#     return max(profit)

def max_profit(prices):
    min_price = 100000
    profit = 0
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit

