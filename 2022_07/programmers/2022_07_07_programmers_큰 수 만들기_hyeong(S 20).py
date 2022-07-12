def solution(number, k):
    result = []
    for i in number:
        while result and result[-1] < i and k > 0:
            result.pop()
            k -= 1
        result.append(i)
    result = ''.join(result)
    if k > 0:
        result = result[:-k]

    return result

a = solution("1924", 2)
b = solution("1231234", 3)
c = solution("4177252841", 4)
d = solution("987654321", 2)

print(a)
print(b)
print(c)
print(d)