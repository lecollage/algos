def isGood(fieldLength: int, maxBoatLength: int):
   # print('START isGood', fieldLength, maxBoatLength)

   freeSpace = fieldLength
   K = maxBoatLength
   boatCount = 1

   while freeSpace > 0 and K > 0:
      freeSpace = freeSpace-(K+1)*boatCount
      boatCount = boatCount+1
      K = K - 1

   freeSpace = freeSpace + 1

   # print(maxBoatLength, K, freeSpace)

   return freeSpace >= 0 and K == 0

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