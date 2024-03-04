def calc(intervals):
    if not len(intervals):
        return 0

    intervals.sort(key=lambda tup: (tup[1],tup[0]))
    print(intervals)

    champInteval = intervals[0]
    removed = set()

    for i in range(1, len(intervals)):
        interval = intervals[i]
        left = interval[0]
        right = interval[1]

        if right <= champInteval[0] or left == champInteval[1]:
            removed.add(i)
        else:
            champInteval = interval

    print(removed)

    return len(intervals) - len(removed)



# n = int(input())

# intervals = []

# for i in range(0, n):
#     left, right = map(int, input().split())
#     intervals.append([left, right])

# print(calc(intervals))
        


inputs = [
    # [
    #     [2, 3],
    #     [4, 5],
    #     [1, 3],
    #     [5, 10],
    # ],
    # [
    #     [1, 2],
    #     [2, 3],
    #     [4, 5],
    #     [4, 5],
    #     [5, 6],
    # ],
    # [
    #     [1, 50],
    #     [49, 50],
    # ],
    # [
    #     [1, 50],
    #     [50, 51],
    #     [10, 20],
    #     [21, 30],
    # ],
    # [],
    # [
        # [1, 1]
    # ],
    # [
    #     [0, 0]
    # ],

    [
        [1, 15],
        [3, 8],
        [1, 4],
        [18, 20],
        [3, 5],
        [8, 12],
        [8, 18],
        [2, 9],
        [6, 10],
        [14, 17],
    ],
]

for intervals in inputs:
   print(calc(intervals))

'''
3
1 3
2 3
4 5
'''