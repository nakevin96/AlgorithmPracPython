def solution(numbers):
    def fill_zero(b_list):
        curr_len = len(b_list)
        k = 0
        while 2 ** k - 1 < curr_len:
            k += 1
        fz_list = ['0' for _ in range((2 ** k - 1) - curr_len)]
        fz_list.extend(b_list)
        return fz_list

    def is_established(b_list):
        if len(b_list) == 3:
            if b_list[1] == '1':
                return 1
            elif b_list[1] == '0' and (b_list[0] == '1' or b_list[2] == '1'):
                return -1
            return 0

        mid_idx = len(b_list) // 2
        left_result = is_established(b_list[:mid_idx])
        right_result = is_established(b_list[mid_idx + 1:])

        if left_result == -1 or right_result == -1:
            return -1
        elif left_result == 0 and right_result == 0:
            if b_list[mid_idx] == '1':
                return 1
            else:
                return 0
        elif b_list[mid_idx] == '0':
            if left_result == 1 or right_result == 1:
                return -1
            return 0
        return 1

    result = []

    for number in numbers:
        if number == 1:
            result.append(1)
            continue
        binary_list = list(str(bin(number)))[2:]
        binary_list = fill_zero(binary_list)
        if is_established(binary_list) == -1:
            result.append(0)
        else:
            result.append(1)
    return result
