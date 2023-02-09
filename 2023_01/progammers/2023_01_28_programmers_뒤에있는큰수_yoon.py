def solution(numbers):
    result = []
    numbers.reverse()
    stack = []
    for n in numbers:
        while stack and stack[-1] <= n:
            stack.pop()
        if not stack:
            result.append(-1)
            stack.append(n)
            continue
        result.append(stack[-1])
        stack.append(n)
    result.reverse()
    return result