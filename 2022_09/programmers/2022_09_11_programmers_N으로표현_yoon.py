def solution(N, number):
    # number이 N이면 바로 1 반환
    if number == N:
        return 1

    # dynamic table dt 생성
    # dt[i]는 N을 i번 사용해서 만들 수 있는 숫자 집합
    # in으로 연산할 것이라 list아닌 set사용
    dt = [set() for _ in range(9)]

    # 순회를 2부터 돌 예정이라 N을 한 번만 사용하는 경우인 dt[1]에 N추가
    dt[1].add(N)

    # N을 2번 쓰는 경우부터 8번 쓰는 경우까지 반복
    # 예를 들어 2번쓰는 경우 -> N 0번써서 만들 수 있는 수, 2번써서 만들수 있는 수 사이의 사칙연산으로 나오는 값
    # N을 1번 써서 만들 수 있는 수와 N을 1번 써서 만들 수 있는 수 사이의 사칙연산으로 나오는 값들의 집합
    # 3번 쓰는 경우는 (0, 3) (1, 2) 로 쪼갤 수 있음
    for num_of_N in range(2, 9):
        # dt[num_of_N] 과 dt[0] 사이의 사칙연산은 N이 num_of_N만큼 붙어있는 경우 뿐
        dt[num_of_N].add(int(f'{N}' * num_of_N))

        # 2: (0, 0) (1,1) // 3: (0, 3) (1, 2) // 4: (0, 4) (1, 3) (2, 2)
        # 5: (0, 5) (1, 4) (2, 3) 이런식으로 짝지어서 사칙연산 진행
        for set1_num in range(1, (num_of_N // 2) + 1):
            set2_num = num_of_N - set1_num
            for item1 in dt[set1_num]:
                for item2 in dt[set2_num]:
                    # 덧셈과 곱셈은 앞 뒤 바뀌어도 결과 동일
                    dt[num_of_N].add(item1 + item2)
                    dt[num_of_N].add(item1 * item2)

                    # 뺄셈 나눗셈은 앞 뒤 바뀌면 결과 달라짐
                    dt[num_of_N].add(item1 - item2)
                    dt[num_of_N].add(item2 - item1)

                    # 0으로 나누면 에러 떠서 조건문 사용
                    if item1 != 0:
                        dt[num_of_N].add(item2 // item1)
                    if item2 != 0:
                        dt[num_of_N].add(item1 // item2)

        # dt[num_of_N] 다 만들고 그 안에 num_of_N있으면 결과 반환
        if number in dt[num_of_N]:
            return num_of_N

    # 반복문 나오면 최솟값이 8보다 크단 뜻이니 -1 반환
    return -1
