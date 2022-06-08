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
        for i in range(-1, -m - 1, -1):
            for j in range(n):
                row = i
                while True:
                    if row - 1 == -m - 1 or 'X' not in board[i]:
                        break
                    if board[i][j] == 'X' and board[row - 1][j] != 'X':
                        board[i][j] = board[row - 1][j]
                        board[row - 1][j] = 'X'
                        continue
                    row -= 1

    for i in range(m):
        score += board[i].count('X')

    return score


# [['C', 'C', 'B', 'D', 'E'], ['X', 'X', 'X', 'D', 'E'], ['X', 'X', 'X', 'B', 'F'], ['C', 'C', 'B', 'B', 'F']]

# print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# print(solution(5, 6, ['AAAAAA', 'BBAATB', 'BBAATB', 'JJJTAA', 'JJJTAA']))
print(solution(6, 6, ['IIIIOO', 'IIIOOO', 'IIIOOI', 'IOOIII', 'OOOIII', 'OOIIII']))