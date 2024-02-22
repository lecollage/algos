from typing import List

dict = {
    "": ["(", "["],
    "(": ["(", "[", ")"],
    ")": ["(", ")", "[", "]"],
    "[": ["[", "(", "]"],
    "]": ["(", ")", "[", "]"],
}

def calc(N: int, stack: List[int], path: str): 
    if N == 0 and not stack:
        print(''.join([str(i) for i in path]))
        return

    if N == 0:
        return 

    possibleElems = dict[stack[-1]] if stack else dict[""]

    for el in possibleElems:
        newStack = [*stack]

        if stack:
            if stack[-1] == "(" and el == ")":
                newStack.pop()
                calc(N-1, newStack, [*path, ")"])
            elif stack[-1] == "[" and el == "]":
                newStack.pop()
                calc(N-1, newStack, [*path, "]"])
            else:
                newStack.append(el)
                calc(N-1, newStack, [*path, el])
        else:
            newStack.append(el)
            calc(N-1, newStack, [*path, el])


N = int(input())

calc(N, [], "")
