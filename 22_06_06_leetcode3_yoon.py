class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 길이 0짜리 들어왔을 때 반환할 수 있게 0으로 초기화
        max_len = 0
        # 나왔던 char가 들어갈 curr_list 생성
        curr_list = []

        # s 순차적 접근
        for c in list(s):
            # c가 curr_list에 없을 때 붙여줌
            if c not in curr_list:
                curr_list.append(c)
            else:
                # c가 curr_list에 있다면
                # max_len을 업데이트하고
                max_len = max(max_len, len(curr_list))
                # 중복된 문자 다음부터 들어갈 수 있도록 curr_list 변경
                curr_list = curr_list[curr_list.index(c) + 1:]
                # 그 후 c를 붙여줌
                curr_list.append(c)

        # max_len을 바로바로 업데이트 하지 않았기 때문에 마지막에 curr_list길이와
        # max_len 비교
        return max(max_len, len(curr_list))


class Solution2:
    def lengthOfLongestSubstring2(self, s: str) -> int:
        # 중복된 문자가 나왔었는지 나왔었다면 어느 위치에 나왔었는지
        # dictionary에 저장하면 빠르게 탐색할 수 있을 것 같아서 사용
        used_char = {}
        # start는 길이를 찾아내기 위한 포인터
        start = 0
        # max_len은 혹시 빈 문자열이 들어오면 0을 반환할 수 있게 0으로 초기화
        max_len = 0

        # s에 enumerate적용해서 순차적으로 접근
        for idx, char in enumerate(list(s)):
            # 만약에 char가 사용된적이 있고, start값(현재 중복이 없다고 체크된
            # 문자중 가장 첫번째 위치)이 used_char[char]보다 작을 때 start갱신
            if char in used_char and start <= used_char[char]:
                start = used_char[char] + 1
            else:
                # 중복 되지 않았다면 max_len을 바로바로 갱신
                max_len = max(max_len, idx - start + 1)

            used_char[char] = idx
        return max_len
