def leetalgo(strs):
    strsdict = {}

    # for i in strs:
    #     if ''.join(sorted(i)) in strsdict:
    #         strsdict[''.join(sorted(i))] += [i]
    #     else:
    #         strsdict[''.join(sorted(i))] = [i]
    # return strsdict.values()

    for i in strs:
        sorted_strs = ''.join(sorted(i))
        if sorted_strs in strsdict:
            strsdict[sorted_strs] += [i]
        else:
            strsdict[sorted_strs] = [i]

    return list(strsdict.values())


list = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(leetalgo(list))