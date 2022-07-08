class Solution:
    def isValid(self, s: str) -> bool:

        for i in range(len(s)):
            if s[i] == '{' and s[i + 1] != '}':
                return False
            elif s[i] == '[' and s[i + 1] != ']':
                return False
            elif s[i] == '(' and s[i + 1] != ')':
                return False
        return True

        # for i in range(len(s)):
        #     if s[i] == '{':
        #         if s[i + 1] != '}':
        #             return False
        #     elif s[i] == '[':
        #         if s[i + 1] != ']':
        #             return False
        #     elif s[i] == '(':
        #         if s[i + 1] != ')':
        #             return False
        # return True
inputval = Solution()
input1 = "()"  # result -> True
input2 = "()[]{}"  # result -> True
input3 = "(]"  # result -> False

print(inputval.isValid(input2))
