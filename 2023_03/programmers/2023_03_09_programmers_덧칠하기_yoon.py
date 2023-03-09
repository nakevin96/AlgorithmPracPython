def solution(n, m, section):
    next_section = 1
    result = 0
    for section_num in section:
        if section_num >= next_section:
            next_section = section_num + m
            result += 1
        if next_section > n:
            break
    return result