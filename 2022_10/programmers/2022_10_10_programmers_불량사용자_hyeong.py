# https://school.programmers.co.kr/learn/courses/30/lessons/64064

def compare_id(id1: str, id2: str) -> bool:
    if len(id1) != len(id2):
        return False
    for i in range(len(id1)):
        if id2[i] == '*' or id1[i] == id2[i]:
            continue
        else:
            return False
    return True


def solution(user_id, banned_id):
    result = set()
    temp = []
    def store(id1: str, id2: str, idx: int):
        if idx == len(id2):
            test = sorted(temp)
            result.add(tuple(test))
            return

        for i in range(len(id1)):
            if id1[i] in temp:
                continue
            if compare_id(id1[i], id2[idx]):
                temp.append(id1[i])
                store(id1, id2, idx + 1)
                temp.pop()
    
    idx = 0
    store(user_id, banned_id, idx)
    return len(result)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))