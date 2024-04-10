def calcShipsSpace(k: int):
    cntSpaces = max((1+k)*k//2-1, 0)
    sumOfBigShips = (k+k**2)*k//2
    sumOfExcess = k*(k+1)*(2*k+1)//6-(1+k)*k//2

    return cntSpaces + sumOfBigShips - sumOfExcess

def isGood(fieldLength: int, maxShipLength: int):
   # print('START isGood', fieldLength, maxShipLength)
   return fieldLength >= calcShipsSpace(maxShipLength)

def binSearch(fieldLength: int) -> int:
   if fieldLength == 1:
       return 1

   left = 0
   right = fieldLength

   while(right-1 > left):
       middle = int(left + (right-left)/2)
       
       if isGood(fieldLength, middle):
           left = middle
       else:
           right = middle

   return left

L = int(input())
print(binSearch(L))

# # TEST
inputs = [
    [
       7,
       2
    ],
    [
       0,
       0
    ],
    [
       1,
       1
    ],
    [
       2,
       1
    ],
    [
       15,
       3
    ],
    [
       49,
       5
    ],
    [
       55,
       5
    ],
]

for i, input in enumerate(inputs):
    print('result', binSearch(input[0]) == input[1])

'''
7

2
'''