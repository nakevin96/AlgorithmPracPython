# https://school.programmers.co.kr/learn/courses/30/lessons/152995

# 정답 풀이
def solution(scores):
    from collections import defaultdict
    result = 0
    a, b = scores.pop(0)
    total_score = a + b
    rank = defaultdict(int)
    
    scores = list(filter(lambda x: sum(x) > total_score, scores))
    
    for score in scores:
        temp_score = sum(score)
        rank[temp_score] += 1
        
    compare_score = sorted(scores, key=lambda x: (x[0], -x[1]), reverse=True)
    
    for temp in compare_score:
        t_a, t_b = temp
        if a < t_a and b < t_b:
            return -1    
    
    max_b_score = 0
    for index, val in enumerate(compare_score):
        v_a, v_b = val
        if max_b_score <= v_b:
            max_b_score = max(max_b_score, v_b)
        else:
            rank[v_a + v_b] -= 1
            
    for ra in rank:
        result += rank[ra]
    
    return result + 1


# 첫 번째 풀이 실패 10개
def solution(scores):
    from collections import defaultdict
    result = 0
    a, b = scores.pop(0)
    total_score = a + b
    rank = defaultdict(list)
    max_score = 0
    for score in scores:
        temp_score = score[0] + score[1]
        max_score = max(max_score, temp_score)
        rank[temp_score].append(score)
        
    max_score_list = rank[max_score]
    
    for m_score in max_score_list:
        m_a, m_b = m_score[0], m_score[1]
        if a < m_a and b < m_b:
            return -1
    
    for score in scores:
        s_a, s_b = score[0], score[1]
        s_t = s_a + s_b
        if s_t == max_score:
            continue
        for m_score in max_score_list:
            m_a, m_b = m_score[0], m_score[1]
            if s_a < m_a and s_b < m_b:
                rank[s_t].remove(score)
                break
    for ra in rank:
        if ra and ra > total_score:
            result += len(rank[ra])
    
    return result + 1


# 두 번째 풀이 21, 24, 25 시간초과
def solution(scores):
    from collections import defaultdict
    result = 0
    a, b = scores.pop(0)
    total_score = a + b
    rank = defaultdict(list)
    max_score = 0
    
    for score in scores:
        temp_score = score[0] + score[1]
        max_score = max(max_score, temp_score)
        rank[temp_score].append(score)
        
    scores.sort(key=lambda x: x[0]+x[1])
    compare_score = sorted(scores, key=lambda x: x[0]+x[1], reverse=True)
    
    for temp in compare_score:
        t_a, t_b = temp[0], temp[1]
        if a < t_a and b < t_b:
            return -1
    
    for score in scores:
        s_a, s_b = score[0], score[1]
        for temp in compare_score:
            t_a, t_b = temp[0], temp[1]
            if s_a < t_a and s_b < t_b:
                rank[s_a + s_b].remove(score)
                break
    
    for ra in rank:
        if ra and ra > total_score:
            result += len(rank[ra])
    
    return result + 1