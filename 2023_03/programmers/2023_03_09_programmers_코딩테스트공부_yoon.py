# 빼다가 실패한 코드
# def solution(alp, cop, problems):
#     target_alp, target_cop = 0, 0
#     for prob in problems:
#         target_alp = max(target_alp, prob[0])
#         target_cop = max(target_cop, prob[1])
#
#     if target_alp <= alp and target_cop <= cop:
#         return 0
#
#     dp = [[0 for _ in range(target_cop + 1)] for _ in range(target_alp + 1)]
#     for r in range(target_alp + 1):
#         for c in range(target_cop + 1):
#             if r <= alp and c <= cop:
#                 continue
#             if r > alp:
#                 dp[r][c] += r - alp
#             if c > cop:
#                 dp[r][c] += c - cop
#
#     # r : alp , c: cop
#     for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
#         target_alp = max(target_alp, alp_req)
#         target_cop = max(target_cop, cop_req)
#         for r in range(min(alp, target_alp), target_alp + 1):
#             for c in range(min(cop,target_cop), target_cop + 1):
#                 if r - alp_rwd < alp_req or c - cop_rwd < cop_req:
#                     continue
#                 # 해당 문제를 풀 수 있는 상황
#                 dp[r][c] = min(dp[r][c], dp[r - alp_rwd][c - cop_rwd] + cost)
#     return dp[target_alp][target_cop]

def solution(alp, cop, problems):
    target_alp, target_cop = 0, 0
    for prob in problems:
        target_alp = max(target_alp, prob[0])
        target_cop = max(target_cop, prob[1])


    dp = [[0 for _ in range(target_cop + 1)] for _ in range(target_alp + 1)]
    for r in range(target_alp + 1):
        for c in range(target_cop + 1):
            if r <= alp and c <= cop:
                continue
            if r > alp:
                dp[r][c] += r - alp
            if c > cop:
                dp[r][c] += c - cop

    # r : alp , c: cop
    for r in range(min(alp, target_alp), target_alp + 1):
        for c in range(min(cop,target_cop), target_cop + 1):
            if r + 1 <= target_alp:
                dp[r + 1][c] = min(dp[r + 1][c], dp[r][c] + 1)
            if c + 1 <= target_cop:
                dp[r][c + 1] = min(dp[r][c + 1], dp[r][c] + 1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp_req <= r and cop_req <= c:
                    increased_r = min(target_alp, r + alp_rwd)
                    increased_c = min(target_cop, c + cop_rwd)
                    dp[increased_r][increased_c] = min(dp[increased_r][increased_c], dp[r][c] + cost)

    return dp[target_alp][target_cop]