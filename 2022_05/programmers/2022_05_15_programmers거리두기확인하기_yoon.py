def solution(places):
    def p_check(struct, row, col):
        if row - 1 >= 0 and struct[row - 1][col] == 'P':
            return 0
        elif col + 1 <= 4 and struct[row][col + 1] == 'P':
            return 0
        elif row + 1 <= 4 and struct[row + 1][col] == 'P':
            return 0
        elif col - 1 >= 0 and struct[row][col - 1] == 'P':
            return 0
        else:
            return 1

    def o_check(struct, row, col):
        count = 0
        if row - 1 >= 0 and struct[row - 1][col] == 'P':
            count += 1
        if col + 1 <= 4 and struct[row][col + 1] == 'P':
            count += 1
        if row + 1 <= 4 and struct[row + 1][col] == 'P':
            count += 1
        if col - 1 >= 0 and struct[row][col - 1] == 'P':
            count += 1
        if count >= 2:
            return 0
        return 1

    def test(place_list):
        structure = []
        for place in place_list:
            structure.append(list(place))
        for row_idx in range(len(structure)):
            for col_idx in range(len(structure[0])):
                if structure[row_idx][col_idx] == 'P':
                    if p_check(structure, row_idx, col_idx) == 0:
                        return 0
                elif structure[row_idx][col_idx] == 'O':
                    if o_check(structure, row_idx, col_idx) == 0:
                        return 0
        return 1

    answer = []
    for place in places:
        answer.append(test(place))
    return answer