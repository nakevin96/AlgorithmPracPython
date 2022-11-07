def solution(n, lighthouse):
    from collections import defaultdict

    house_info = defaultdict(list)
    for h1, h2 in lighthouse:
        house_info[h1].append(h2)
        house_info[h2].append(h1)

    light_set = set()
    while house_info:
        house_info_keys = list(house_info.keys())
        for h_id in house_info_keys:
            if h_id in house_info and len(house_info[h_id]) == 1:
                light_house = house_info[h_id][0]
                light_set.add(light_house)
                light_house_adj_info = house_info[light_house]
                del house_info[light_house]

                for adj_house in light_house_adj_info:
                    if adj_house in house_info:
                        house_info[adj_house].remove(light_house)
                        if not house_info[adj_house]:
                            del house_info[adj_house]

    return len(light_set)