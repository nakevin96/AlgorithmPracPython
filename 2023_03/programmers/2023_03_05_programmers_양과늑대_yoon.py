def solution(info, edges):
    result = []

    def check_node(sheep_count, wolf_count):
        if sheep_count <= wolf_count:
            return
        result.append(sheep_count)
        for source, target in edges:
            if source in visited_set and target not in visited_set:
                is_sheep = True if info[target] == 0 else False
                visited_set.add(target)
                if is_sheep:
                    check_node(sheep_count + 1, wolf_count)
                else:
                    check_node(sheep_count, wolf_count + 1)
                visited_set.remove(target)

    visited_set = {0}
    check_node(1, 0)
    return max(result)
