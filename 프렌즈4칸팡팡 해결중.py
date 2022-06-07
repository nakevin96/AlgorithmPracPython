def solution(m, n, board):  # m->행 n->열
    poplist = []
    score = 0
    for i in range(m):  # 문자열 입력을 List로 바꾸어줌
        board[i] = list(board[i])

    while True:
        del poplist[:]
        for i in range(m - 1):  # 4칸이 같은 칸을 왼쪽위 좌표만 poplist에 저장함
            for j in range(n - 1):
                if board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i + 1][j] == \
                        board[i + 1][j + 1] and board[i][j] != 'X':
                    poplist.append([i, j])
        if not poplist:
            break
        for i in range(len(poplist)):
            board[poplist[i][0]][poplist[i][1]] = 'X'
            board[poplist[i][0]][poplist[i][1] + 1] = 'X'
            board[poplist[i][0] + 1][poplist[i][1]] = 'X'
            board[poplist[i][0] + 1][poplist[i][1] + 1] = 'X'
        for i in range(1, m, -1):  # 가장 밑에 있는 행부터 시작해서
            while 'X' in board[i]:  # 'X'가 없을때까지 반복함
                row = i  # 바로 윗 자리에 'X'가 없을시 하나씩 줄이면서 위에 행으로 감
                while board[i][board[i].index('X')] != 'X':  # 해당 행에 'X'가 존재하지 않을때까지 반복
                    board[i][board[i].index('X')] = board[row - 1][board[i].index('X')]
                    row -= 1
                board[row - 1][board[i].index('X')] = 'X'
    for i in range(m):
        score += board[i].count('X')

    return score


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
