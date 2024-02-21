from typing import List

dict = {
    "": ["(", "["],
    "(": [")", "[", "("],
    ")": ["(", "[", ")", "]"],
    "[": ["(", "[", "]"],
    "]": ["(", ")", "[", "]"],
}

def calc(N: int, stack: List[int], path: str): 
    # print(N, stack, path)

    if N == 0 and not stack:
        print(' '.join([str(i) for i in path]))
        print()
        return
    
    if N == 0:
        return 

    possibleElems = dict[stack[-1]] if stack else dict[""]

    # print(possibleElems)
    
    for el in possibleElems:
        if stack:
            if stack[-1] == "(" and el == ")":
                stack.pop()
                calc(N-1, stack, [*path, ")"])
            elif stack[-1] == "[" and el == "]":
                stack.pop()
                calc(N-1, stack, [*path, "]"])
        else:
            calc(N-1, [*stack, el], [*path, el])
    
  


N = int(input())

calc(N, [], "")


'''

'''
