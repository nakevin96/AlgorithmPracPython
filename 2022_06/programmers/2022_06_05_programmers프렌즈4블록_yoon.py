def solution(m, n, board):
    for i in range(len(board)):
        board[i] = list(board[i])

    def check_square(row, col, board):
        if board[row][col] != board[row + 1][col]:
            return False
        elif board[row][col] != board[row][col + 1]:
            return False
        elif board[row][col] != board[row + 1][col + 1]:
            return False
        return True

    count = 0
    while True:
        del_point_list = []
        for row_idx in range(m - 1):
            for col_idx in range(n - 1):
                if board[row_idx][col_idx] == 'X':
                    continue
                if check_square(row_idx, col_idx, board):
                    del_point_list.append((row_idx, col_idx))
                    del_point_list.append((row_idx + 1, col_idx))
                    del_point_list.append((row_idx, col_idx + 1))
                    del_point_list.append((row_idx + 1, col_idx + 1))
        if del_point_list:
            count += len(set(del_point_list))
            for row_idx, col_idx in list(set(del_point_list)):
                board[row_idx][col_idx] = 'X'

            for row_idx, col_idx in reversed(list(set(del_point_list))):
                upper_row_idx = row_idx - 1
                under_row_idx = row_idx

                while upper_row_idx >= 0:
                    if board[under_row_idx][col_idx] == 'X' and board[upper_row_idx][col_idx] != 'X':
                        board[under_row_idx][col_idx], board[upper_row_idx][col_idx] = board[upper_row_idx][col_idx], \
                                                                                       board[under_row_idx][col_idx]
                        under_row_idx -= 1
                        upper_row_idx = under_row_idx - 1
                        continue
                    upper_row_idx -= 1
        else:
            break
    return count