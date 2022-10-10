# 타임 아웃 하나 나온거
# def solution(user_id, banned_id):
#     import re
#     from collections import defaultdict
#     from itertools import product
#
#     possible_dict = defaultdict(list)
#     banned_id_len = len(banned_id)
#
#     banned_id_fixed = [b.replace("*", ".") for b in banned_id]
#
#     for b_idx, b_id in enumerate(banned_id_fixed):
#         tmp_count = 0
#         for u_id in user_id:
#             if len(b_id) != len(u_id):
#                 continue
#             elif re.fullmatch(b_id, u_id) != None:
#                 possible_dict[b_idx].append(u_id)
#
#     possible_list = list(possible_dict.values())
#
#     candidate_list = list(map(sorted, map(set, list(product(*possible_list)))))
#     candidate_list = [tuple(c) for c in candidate_list if len(c) == banned_id_len]
#
#     return len(set(candidate_list))


def solution(user_id, banned_id):
    import re
    from itertools import permutations
    answer = list()
    banned_id_len = len(banned_id)

    banned_id_fixed = [b.replace("*", ".") for b in banned_id]

    for user_id_candidate in permutations(user_id, banned_id_len):
        count = 0
        for u_id, b_id in zip(user_id_candidate, banned_id_fixed):
            if len(u_id) != len(b_id):
                continue
            elif re.fullmatch(b_id, u_id):
                count += 1
        if count == banned_id_len:
            if set(user_id_candidate) not in answer:
                answer.append(set(user_id_candidate))

    return len(answer)