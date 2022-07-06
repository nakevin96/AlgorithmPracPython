from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    queue = deque()
    queue.append((begin, 0))
    checked = [0 for _ in range(len(words))]

    while queue:
        next_word, move_val = queue.popleft()
        if next_word == target:
            return move_val

        for word_idx in range(len(words)):
            diff_val = 0
            for idx in range(len(target)):
                if next_word[idx] != words[word_idx][idx]:
                    diff_val += 1
            if diff_val == 1 and checked[word_idx] == 0:
                queue.append((words[word_idx], move_val + 1))

