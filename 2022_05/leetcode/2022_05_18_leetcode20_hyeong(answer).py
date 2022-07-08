input2 = "()[]{}"
input23 = "({})"
input33 = ")))"

def Solution(s):
    slist = []
    match = {'{': '}', '[': ']', '(': ')'}

    # ( ]
    for i in s:
        if i in match:
            slist.append(i)
        else: # i -> } , pop -> (
            if not slist or match[slist.pop()] != i:
                return False

    return not slist

print(Solution(input33))
