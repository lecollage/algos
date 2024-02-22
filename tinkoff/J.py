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
        if stack:
            if stack[-1] == "(" and el == ")":
                newStack = [*stack]
                newStack.pop()
                calc(N-1, newStack, [*path, ")"])
            elif stack[-1] == "[" and el == "]":
                newStack = [*stack]
                newStack.pop()
                calc(N-1, newStack, [*path, "]"])
            else:
                calc(N-1, [*stack, el], [*path, el])
        else:
            calc(N-1, [*stack, el], [*path, el])


N = int(input())

calc(N, [], "")
