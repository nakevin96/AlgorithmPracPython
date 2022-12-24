# https://school.programmers.co.kr/learn/courses/30/lessons/17680

# deque로 다시 풀어보기

def solution(cacheSize, cities):
    cities = [x.lower() for x in cities]
    cache = set()
    result = 0
    time = 0
    
    for i in cities:
        time += 1
        temp_cache = [x[0] for x in cache]
        if i in temp_cache:
            for j in cache:
                if i == j[0]:
                    cache.remove(j)
                    cache.add((i, time))
                    continue
            result += 1
            continue
            
        result += 5
        if len(cache) < cacheSize:
            cache.add((i, time))
        else:
            if cacheSize < 2:
                continue
            Recent_val = min(cache, key=lambda x:x[1])
            cache.remove(Recent_val)
            cache.add((i, time))
    
    return result