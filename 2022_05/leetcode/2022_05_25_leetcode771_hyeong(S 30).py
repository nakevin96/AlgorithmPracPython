class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        stones = list(stones)

        for i in range(len(stones)):
            if stones[i] in jewels:
                count += 1

        return count

a = Solution()

jewels = 'aA'
stones = 'aAAbbbb'

aresult = a.numJewelsInStones(jewels, stones)

print(aresult)