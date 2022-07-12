from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    queue = deque()
    queue.append((len(words), 0))
    words.append(begin)
    checked = [0 for _ in range(len(words))]

    while queue:
        next_word_idx, move_val = queue.popleft()
        checked[next_word_idx] = 1
        if words[next_word_idx] == target:
            return move_val

        for word_idx in range(len(words)):
            diff_val = 0
            for idx in range(len(target)):
                if words[next_word_idx][idx] != words[word_idx][idx]:
                    diff_val += 1
            if diff_val == 1 and checked[word_idx] == 0:
                queue.append((word_idx, move_val + 1))

    return 0
