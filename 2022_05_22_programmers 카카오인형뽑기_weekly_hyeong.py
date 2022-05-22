def solution(board, moves):
    popdoll = 0  # 터뜨린 인형 수
    basket = [0]  # 인형 담을 리스트 -> 12번째 줄에
    # basket 마지막 담긴것이 없을때 실행이 되지 않기 때문에 없는인형을 추가해준다
    boarddict = dict()

    for i in range(len(board)):  # 2차원 배열을 dict에 넣는다
        boarddict[i + 1] = board[i]

    for i in moves:  # moves -> 인형뽑기 위치
        for j in range(1, (len(boarddict) + 1)):  # 인형뽑기 위치에 0 이 아닌것을 찾도록 길이만큼 반복
            if boarddict[j][i - 1] != 0:  # boaeddict key 의 moves 자리가 0이 아닐때
                if basket[-1] == boarddict[j][i - 1]:
                    basket.pop()
                    popdoll += 2
                    boarddict[j][i - 1] = 0
                    break
                basket.append(boarddict[j][i - 1])  # basket에 그 숫자 인형을 추가한다.
                boarddict[j][i - 1] = 0
                break
    return popdoll


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))
