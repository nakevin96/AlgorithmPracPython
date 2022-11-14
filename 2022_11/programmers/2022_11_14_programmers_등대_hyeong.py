# https://school.programmers.co.kr/learn/courses/30/lessons/133500
from collections import defaultdict

def solution(n, lighthouse):
    path_dict = defaultdict(list)
    
    for a, b in lighthouse:
        path_dict[a].append(b)
        path_dict[b].append(a)
    
    # path_dict를 모두 돌면서 key의 value가 하나 있는 곳을 먼저 체크 한다.
    # 체크 한 후 path_dict에 존재하는지도 체크한다 - 없으면 물려있는 상대 노드에 관련있는
    # 모든 노드를 제거 한다.
    # result += 1을 한다
    
    result = 0
    # while path_dict:
    #     for end_node, side_node in path_dict.items():
    #         # if not side_node:
    #         #     # del(path_dict[end_node])
    #         #     del path_dict[end_node]
    #         if len(side_node) == 1: # val 이 중심, key 가 끝 노드
    #             del_val = [x for x in path_dict[side_node[0]]] # 끝에 달려있는거 저장
    #             need_remove_node = side_node[0]
    #             # del(path_dict[side_node[0]]) # 중심 노드 제거 # 1
    #             del path_dict[side_node[0]]
    #             for key, val in path_dict.items():
    #                 if need_remove_node in val:
    #                     val.remove(need_remove_node)
    #             result += 1
    
    # while path_dict:
    #     for end_node, side_node in path_dict.items():
    #         if len(side_node) == 1:
    #             del_val = [x for x in path_dict[side_node[0]]]
    #             need_remove_node = side_node[0]
    #             result += 1
    #             break
    #     del_list = []
    #     if need_remove_node:
    #         del(path_dict[need_remove_node])

    #     for key, val in path_dict.items():
    #         if need_remove_node in val:
    #             val.remove(need_remove_node)
    #             if not val:
    #                 del_list.append(key)
    #     for dl in del_list:
    #         del(path_dict[dl])
    #     need_remove_node = 0

    print(path_dict)

    while path_dict:
        for end_node, side_node in path_dict.copy().items():
            if len(side_node) == 1 and end_node in path_dict:
                temp = side_node[0]
                del_node_list = [x for x in path_dict[temp]]
                del path_dict[temp]
                for i in del_node_list:
                    path_dict[i].remove(temp)
                    if not path_dict[i]:
                        del path_dict[i]
                result += 1

    return result

print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))
print(solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))