import math
from collections import defaultdict


def solution(fees, records):
    def calculate_fee(total_time):
        if total_time <= base_time:
            return base_cost
        else:
            return base_cost + (math.ceil((total_time - base_time) / extra_time) * extra_cost)

    result_dict = defaultdict(int)
    record_dict = defaultdict(list)
    base_time, base_cost, extra_time, extra_cost = fees
    end_time = (23 * 60) + 59
    for r_string in records:
        r_time, r_car_id, r_action = r_string.split()
        r_h, r_m = r_time.split(":")
        r_time = (int(r_h) * 60) + int(r_m)

        if not record_dict[r_car_id]:
            record_dict[r_car_id].append(r_time)
        else:
            tmp_time = record_dict[r_car_id].pop()
            duration = r_time - tmp_time
            result_dict[r_car_id] += duration
    for record_dict_key in record_dict:
        if record_dict[record_dict_key]:
            tmp_time = record_dict[record_dict_key][0]
            duration = end_time - tmp_time
            result_dict[record_dict_key] += duration

    result = [(rd[0], rd[1]) for rd in result_dict.items()]
    result.sort(key=lambda x: x[0])
    return [calculate_fee(r[1]) for r in result]
