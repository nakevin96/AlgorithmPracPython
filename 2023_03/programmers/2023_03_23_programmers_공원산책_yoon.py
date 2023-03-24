def solution(park, routes):
    row_limit = len(park)
    col_limit = len(park[0])
    dog_pos = [0, 0]

    is_find = False
    for pr in range(row_limit):
        if is_find:
            break
        for pc in range(col_limit):
            if park[pr][pc] == 'S':
                dog_pos = [pr, pc]
                is_find = True
                break
        if is_find:
            break

    direction_dict = {
        'N': [-1, 0],
        'E': [0, 1],
        'S': [1, 0],
        'W': [0, -1]
    }

    for route in routes:
        [direction, dist] = route.split(' ')
        dist = int(dist)
        next_dr = dog_pos[0] + (direction_dict[direction][0] * dist)
        next_dc = dog_pos[1] + (direction_dict[direction][1] * dist)
        if dog_pos[0] == next_dr:
            if next_dc < 0 or next_dc >= col_limit:
                continue
            is_blocked = False
            for mc in range(min(dog_pos[1], next_dc), max(dog_pos[1], next_dc) + 1):
                if park[dog_pos[0]][mc] == 'X':
                    is_blocked = True
                    break
            if is_blocked:
                continue
            dog_pos[1] = next_dc
        else:
            if next_dr < 0 or next_dr >= row_limit:
                continue
            is_blocked = False
            for mr in range(min(dog_pos[0], next_dr), max(dog_pos[0], next_dr) + 1):
                if park[mr][dog_pos[1]] == 'X':
                    is_blocked = True
                    break
            if is_blocked:
                continue
            dog_pos[0] = next_dr
    return dog_pos
