def solution(cap, n, deliveries, pickups):
    result = 0

    while pickups and pickups[-1] == 0:
        pickups.pop()
    while deliveries and deliveries[-1] == 0:
        deliveries.pop()

    while deliveries or pickups:
        curr_pos = 0
        result += len(deliveries) - curr_pos
        curr_pos = len(deliveries)

        curr_cap = cap
        while deliveries and curr_cap - deliveries[-1] >= 0:
            curr_cap -= deliveries.pop()
        if deliveries:
            deliveries[-1] -= curr_cap

        result += (abs(len(pickups) - curr_pos) + len(pickups))

        curr_cap = cap
        while pickups and curr_cap - pickups[-1] >= 0:
            curr_cap -= pickups.pop()
        if pickups:
            pickups[-1] -= curr_cap
    return result