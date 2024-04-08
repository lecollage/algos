def isGood(fieldLength: int, maxBoatLength: int):
   K = maxBoatLength
   T = K+1 # length of the maximum boat + minimum free space
   A = 1+1 # length of the minimum boat + minimum free space
   N = K
   S = int(((T + A) * N)/2 - 1)
   # print(K, S)

   return S <= fieldLength

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
       9,
       3
    ],
    [
       10,
       3
    ],
    [
       11,
       3
    ],
    [
       12,
       3
    ],
    [
       13,
       4
    ],
    [
       10**18,
       1414213560
    ],
]

for i, input in enumerate(inputs):
    print('result', binSearch(input[0]) == input[1])

'''
7

2
'''