from itertools import permutations


def solution(numbers):
    answer = 0

    num_str_list = list(numbers)
    num_per_list = []
    for num_len in range(1, len(num_str_list) + 1):
        num_per_list.extend(list(permutations(num_str_list, num_len)))

    num_per_list = set(num_per_list)
    num_int_list = [int("".join(num_str)) for num_str in num_per_list]

    num_int_list = set(num_int_list)

    for num in num_int_list:
        if num <= 1:
            continue
        is_prime = True
        for check_num in range(2, int(num ** 0.5) + 1):
            if num % check_num == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1

    return answer