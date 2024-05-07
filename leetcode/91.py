class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1 and s[0] != "0":
            return 1
        
        if s[0] == "0":
            return 0

        if len(s) > 2 and int(s[0:2]) > 26 and s[2]=="0":
            return 0

        dp = [0 for _ in range(0, len(s))]

        dp[0] = 1

        i = 1

        while i < len(s):
            pair = s[i-1:i+1]

            # print(pair, int(pair))

            if pair[0] == "0" and pair[1] == "0":
                return 0

            if int(pair) < 27 and pair[0] != "0" and pair[1] != "0":
                if i >= 2 and dp[i+1]!="0":
                    dp[i] = dp[i-1]+dp[i-2]
                else:
                    dp[i] = dp[i-1]+1
            elif pair[1] == "0" and int(pair) < 27 and i > 1 and s[i-2] != "0":
                dp[i] = dp[i-1]-1
            elif pair[1] == "0" and int(pair) >= 27:
                return 0
            else:
                dp[i] = dp[i-1]

            i = i+1

            print(i, dp)

        return dp[-1]

inputs = [
    [
        "2611055971756562",
        4,
    ],

'''
26 11055971756562
2 6 11055971756562
26 1 1055971756562
2 6 1 1055971756562
'''

    # [
    #     "1133",
    #     3,
    # ],
    # [
    #     "11221",
    #     8,
    # ],
    # [
    #     "1123",
    #     5,
    # ],
    # [
    #     "1012",
    #     2,
    # ],
    # [
    #     "10011",
    #     0,
    # ],
    # [
    #     "1123",
    #     5,
    # ],
    # [
    #     "11106",
    #     2,
    # ],
    # [
    #     "1",
    #     1,
    # ],
    # [
    #     "10",
    #     1,
    # ],
    # [
    #     "12",
    #     2,
    # ],
    # [
    #     "1110202",
    #     2,
    # ],
    # [
    #     "06",
    #     0,
    # ],
    # [
    #     "27",
    #     1,
    # ],
    # [
    #     "270",
    #     0,
    # ],
    # [
    #     "1127",
    #     3,
    # ],
]


for _, input in enumerate(inputs):
    solution = Solution()
    print(solution.numDecodings(input[0]) == input[1])

'''

1 1
1 2
1 2
0 2
6 2


'''