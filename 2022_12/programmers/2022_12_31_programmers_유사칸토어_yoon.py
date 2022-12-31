def solution(n, l, r):
    def one_counter(idx):
        # 처음부터 idx까지의 1의 갯수를 카운팅 하는 함수
        # 1 -> 11011 -> 11011 11011 00000 11011 11011 ->
        # 11011 11011 00000 11011 11011 11011 11011 00000 11011 11011 00000 000..

        if idx <= 5:
            return "11011"[:idx].count("1")

        min_square_val = 1
        while 5 ** (min_square_val + 1) <= idx:
            min_square_val += 1

        ## 매개변수 idx와 가장 근접한 5의 거듭제곱을 찾아 min_square_val에
        ## 저장했기 때문에 share는 0, 1, 2, 3, 4, 5중 하나가 나옴
        ## 5의 경우는 idx가 딱 5의 배수인 경우
        divider = 5 ** min_square_val
        share = idx // divider
        remain = idx % divider

        # 1은 처음에 1개 증가하면 4개 -> 16개 -> 64개로 증식하기 때문에
        # share만큼 곱해주고 share가 3인 부분 즉 세번째 묶음은 전부다 0이니까
        # result에서 빼준다
        # share가 2면 remain이 전부 0이라 1을 카운팅 해줄 필요가 없으니 바로 result반환
        # 그 외의 경우 remain에 대해 다시 one_counter호출해서 값 계산
        result = share * (4 ** min_square_val)

        if share == 2:
            return result

        if share >= 3:
            result -= (4 ** min_square_val)

        return result + one_counter(remain)

    return one_counter(r) - one_counter(l - 1)
