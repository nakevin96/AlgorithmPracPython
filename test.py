def solution(m, n, board): # m->행 n->열
    poplist = []

    for i in range(m):
        board[i] = list(board[i])
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i+1][j] == board[i+1][j+1]:
                poplist.append([i, j])
    for i in range(len(poplist)):
        board[i][0] = 'X'
        board[i+1][0] = 'X'
        board[i][1] = 'X'
        board[i+1][1] = 'X'
    for i in m:
        if 'X' in board[i]:
            board[i][board[i].index('X')] = board[i+2]



    return board

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))

# AAA
# AAA