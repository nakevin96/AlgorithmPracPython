class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        stringx = str(x)
        comparex = stringx[::-1]
        if stringx == comparex:
            return True
        else:
            return False

intest1 = 121
test = Solution()

print(test.isPalindrome(intest1))