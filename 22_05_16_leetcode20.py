class Solution:
    def isValid(self, s: str) -> bool:
        char_list = ["(", ")", "{", "}", "[", "]"]
        stack = []
        for c in s:
            if char_list.index(c) % 2 == 0:
                stack.append(c)
            else:
                if not stack:
                    return False
                if char_list.index(stack.pop()) + 1 != char_list.index(c):
                    return False

        return len(stack) == 0