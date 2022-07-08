class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_s = list(str(x))
        check_len = len(list_s) // 2

        for i in range(check_len):
            if list_s[i] != list_s.pop():
                return False

        return True