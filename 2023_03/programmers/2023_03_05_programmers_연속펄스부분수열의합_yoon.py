def solution(sequence):
    # dp[0] => +, dp[1] => -
    dp = [[0 for _ in range(len(sequence))] for _ in range(2)]
    dp[0][0] = sequence[0]
    dp[1][0] = -1 * sequence[0]

    for s_idx in range(1, len(sequence)):
        dp[0][s_idx] = max(sequence[s_idx], dp[1][s_idx - 1] + sequence[s_idx])
        dp[1][s_idx] = max(-1 * sequence[s_idx], dp[0][s_idx - 1] - sequence[s_idx])

    plus_max = max(dp[0])
    minus_max = max(dp[1])
    return max(plus_max, minus_max)
