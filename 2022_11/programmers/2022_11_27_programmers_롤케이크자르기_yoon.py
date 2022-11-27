def solution(topping):
    older = dict()
    younger = set()

    for t in topping:
        if t in older:
            older[t] += 1
        else:
            older[t] = 1

    result = 0
    for t in topping:
        older[t] -= 1
        younger.add(t)
        if older[t] == 0:
            del older[t]
        if len(older) == len(younger):
            result += 1
    return result