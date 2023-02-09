def solution(users, emoticons):
    def get_sale_price_candidates(emoticon_price_list, count):
        if count == 0:
            return [[]]
        result = []
        for idx in range(len(emoticon_price_list)):
            selected = emoticon_price_list[idx]
            for sale in SALE:
                for r in get_sale_price_candidates(emoticon_price_list[idx + 1:], count - 1):
                    result.append([(sale, (100 - sale) * selected // 100), *r])
        return result

    SALE = [10, 20, 30, 40]
    max_subscriber, max_profit = 0, 0
    candidates = get_sale_price_candidates(emoticons, len(emoticons))
    for candidate in candidates:
        tmp_sub = 0
        tmp_profit = 0
        for user_sale_base, user_total_base in users:
            is_over_base = False
            user_sum = 0
            for emo_sale, emo_price in candidate:
                if emo_sale >= user_sale_base:
                    user_sum += emo_price
                if user_sum >= user_total_base:
                    is_over_base = True
                    break
            if is_over_base:
                tmp_sub += 1
            else:
                tmp_profit += user_sum
        if tmp_sub > max_subscriber:
            max_subscriber = tmp_sub
            max_profit = tmp_profit
        elif tmp_sub == max_subscriber and tmp_profit > max_profit:
            max_profit = tmp_profit
    return [max_subscriber, max_profit]
