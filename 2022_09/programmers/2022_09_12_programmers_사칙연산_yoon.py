# 1. 각 숫자에서 계산하는 숫자를 1개 씩 늘려가며 dynamic table 갱신
def solution(arr):
    inf = float('inf')
    number_size = (len(arr) // 2) + 1

    # 3. dynamic table은 최댓값 저장할 테이블과 최솟값 저장할 테이블 필요
    # dt_max[i][j]와 dt_min[i][j]는 각각 i번째 수에서 j번째 수까지 연산을 했을 때
    # 나올 수 있는 최댓값과 최솟값 의미..
    dt_max = [[-inf for _c in range(number_size)] for _r in range(number_size)]
    dt_min = [[inf for _c in range(number_size)] for _r in range(number_size)]

    # 2. 계산할 수의 갯수 루프 돌기
    # n개의 수가 있다면 1개에서 n개까지 돌아야함
    # 1개는 자기 자신이니 바로 저장
    for num_len_1_idx in range(number_size):
        dt_max[num_len_1_idx][num_len_1_idx] = dt_min[num_len_1_idx][num_len_1_idx] = int(arr[2 * num_len_1_idx])

    # 2개에서 n개 처리
    # num_to_add는 뒤에 몇개까지 연산할지 나타냄
    for num_to_add in range(1, number_size):
        # 시작 숫자 인덱스: start number index -> sni
        for sni in range(number_size - num_to_add):
            # 마지막 숫자 인덱스: end number index -> eni
            eni = sni + num_to_add

            # dp: divide point로 어디서 나누어 계산할지..
            # dp를 기준으로 dp포함 전과 dp 제외 후로 나눔
            for dp in range(0, eni):
                # dp기준으로 연산자 가져옴
                # sni, eni, dp모두 dynamic table index이기 때문에
                # arr에 적용하려면 2배해줘야 함
                operator = arr[2 * dp + 1]
                if operator == "-":
                    # 빼기 연산에서 최댓값은 최대 - 최소 최솟값은 최소 - 최대
                    dt_max[sni][eni] = max(dt_max[sni][eni], dt_max[sni][dp] - dt_min[dp + 1][eni])
                    dt_min[sni][eni] = min(dt_min[sni][eni], dt_min[sni][dp] - dt_max[dp + 1][eni])
                elif operator == "+":
                    # 더하기 연산에서 최댓값은 최대 + 최대 최솟값은 최소 + 최소
                    dt_max[sni][eni] = max(dt_max[sni][eni], dt_max[sni][dp] + dt_max[dp + 1][eni])
                    dt_min[sni][eni] = min(dt_min[sni][eni], dt_min[sni][dp] + dt_min[dp + 1][eni])

    return dt_max[0][number_size - 1]
