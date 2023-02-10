def solution2(money, coins):
    if not coins:
        return 0
    coin_len = len(coins)
    dt = [[0 for _c in range(money + 1)] for _r in range(coin_len)]

    for target_money in range(money + 1):
        if target_money % coins[0] == 0:
            dt[0][target_money] = 1

    for coin_idx in range(1, coin_len):
        for target_money in range(money + 1):
            if coins[coin_idx] > target_money:
                dt[coin_idx][target_money] += dt[coin_idx - 1][target_money]
            else:
                dt[coin_idx][target_money] += (dt[coin_idx - 1][target_money] + dt[coin_idx][
                    target_money - coins[coin_idx]]) % 1000000007
                dt[coin_idx][target_money] = dt[coin_idx][target_money] % 1000000007

    return dt[coin_len - 1][money]


def solution(money, coins):
    if not coins:
        return 0
    coins.sort()
    dt = [0 for _ in range(money + 1)]
    dt[0] = 1

    for coin in coins:
        for target_money in range(coin, money + 1):
            dt[target_money] = (dt[target_money] + dt[target_money - coin]) % 1000000007

    return dt[money] % 1000000007
