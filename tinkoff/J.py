from typing import List

dict = {
    "": ["(", "["],
    "(": [")", "[", "("],
    ")": ["(", "[", ")", "]"],
    "[": ["(", "[", "]"],
    "]": ["(", ")", "[", "]"],
}

def pathIsCorrect(path: List[int]):
    if path[-1] == "(" or path[-1] == "[":
        return False
     
    stack = []
    
    for el in path:
        if stack:
            if stack[-1] == "(" and el == ")":
                stack.pop()
            elif stack[-1] == "[" and el == "]":
                stack.pop()
            else:
                stack.append(el)
        else:
            stack.append(el)

    return True if not stack else False
     


def calc(N: int, stack: List[int]): 
    if N == 0:
        if pathIsCorrect(stack):
            print(''.join([str(i) for i in stack]))
        return
    
    possibleElems = ["(","[",  ")", "]"]

    for el in possibleElems:
            calc(N-1, [*stack, el])
    
  
N = int(input())

calc(N, [])

# print(pathIsCorrect("()") == True)
# print(pathIsCorrect("[]") == True)
# print(pathIsCorrect("[") == False)
# print(pathIsCorrect("(") == False)
# print(pathIsCorrect("[]]") == False)
# print(pathIsCorrect("[])") == False)
# print(pathIsCorrect("[[])") == False)
# print(pathIsCorrect("[(])") == False)
# print(pathIsCorrect("[()]") == True)
# print(pathIsCorrect("[[]]") == True)
# print(pathIsCorrect("(())") == True)
# print(pathIsCorrect("(()") == False)
# print(pathIsCorrect("(()]") == False)
# print(pathIsCorrect("]") == False)
# print(pathIsCorrect(")") == False)


'''

'''
