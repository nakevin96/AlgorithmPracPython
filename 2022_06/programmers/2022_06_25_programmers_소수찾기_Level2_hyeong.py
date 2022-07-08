from itertools import permutations
from itertools import combinations

def solution(num: str) -> int:
    count_prime = 0
    num_list = list()

    for i in range(1, len(num) + 1):  # make permutations 1
        num_list += permutations(num, i)

    num_list = list(map(''.join, num_list))
    num_list = list(set([int(i) for i in num_list]))
    check_list = [True for i in range(len(num_list))]

    for i in num_list:
        is_prime = True
        if i == 2:
            count_prime += 1
        if i > 2:
            j = 2
            sqrt = int(i ** 0.5)
            while j <= sqrt + 1:
                if i % j == 0:
                    is_prime = False
                    break

                j += 1
            if is_prime == True:
                count_prime += 1

    return num_list, count_prime
  # 011 0011
# print(solution("17"))
# print(solution("011"))
# print(solution("3"))
print(solution("2"))