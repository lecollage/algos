class Solution:
    def isPalindrome(self, s: str, i, j) -> bool:
        sameLetter = True
        letter = s[i]

        if len(s) == 1:
            return True, sameLetter, letter

        while j-i>=0:
            if s[i] != s[j]:
                return False, False, letter
            else: 
                if letter != s[i]: 
                    sameLetter = False

            i = i+1
            j = j-1

        return True, sameLetter, letter

    def countSubstrings(self, s: str) -> int:
        L = len(s)+1

        if L == 0:
            return 0
        
        if L == 1:
            return 1

        dp = [[0]*L for _ in range(0, L)]
        # print(dp)

        # dp[1][1]=1

        for i in range(1, L):
            dp[i][i] = dp[i][i] + dp[i-1][-1]
            sameLetter = False
            letter = s[i-1]

            for j in range(i, L):
                if sameLetter and letter == s[j-1]:
                    dp[i][j] = dp[i][j-1] + dp[i][j] + 1
                else:
                    isPalindrome, sameLetter, letter = self.isPalindrome(s, i-1, j-1)
                    dp[i][j] = dp[i][j-1] + dp[i][j] + (1 if isPalindrome else 0)

        # print(dp)

        return dp[-1][-1]



inputs = [
    ["abc", 3, 0, 2, False],
    ["aaa", 6, 0, 2, True],
    ["abcba", 5+1+1, 0, 4, True],
    ["abxxba", 6+1+1+1, 0, 5, True],
    [
        "ayeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaah",
        496510, 0, 5, True
    ],
    [
        "dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg",
        77, 0, 5, True
    ],
]
s = Solution()
for input in inputs:
    print(s.countSubstrings(input[0]) == input[1])
    # print(s.isPalindrome(input[0], input[2], input[3]) == input[4])


'''
    
abxxba

abx

xx
bxxb

aaa

a
a
a
aa
aa
aaa
'''