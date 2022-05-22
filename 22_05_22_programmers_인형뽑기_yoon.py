def solution(board, moves):
    def make_dict(board):
        board_len = len(board)
        board_dict = {}
        for row in range(board_len):
            for col in range(board_len):
                if board[row][col] != 0:
                    if col not in board_dict:
                        board_dict[col] = 1
                    else:
                        board_dict[col] += 1
        return board_dict

    item_count = make_dict(board)
    result = 0
    size = len(board)
    stack = []
    for move in moves:
        if item_count[move - 1] == 0:
            continue
        else:
            pick = board[size - item_count[move - 1]][move - 1]
            item_count[move - 1] -= 1
            if stack:
                if stack[-1] != pick:
                    stack.append(pick)
                else:
                    stack.pop()
                    result += 2
            else:
                stack.append(pick)
    return result