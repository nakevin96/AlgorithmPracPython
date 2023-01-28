# https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    result = [-1 for _ in range(len(numbers))]
    stack = []
    for index, val in enumerate(numbers):
        while stack and stack[-1][1] < val:
            result[stack.pop()[0]] = val
        stack.append((index, val))

    return result