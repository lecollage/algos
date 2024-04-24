class Solution:
    def getPalindromesCount(self, s, l, r) -> int:
        length = 0

        if  l >= 0 and r < len(s) and r-l == 1 and s[l] == s[r]:
            length = 1

        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l = l-1
                r = r+1
                length = r-l
            else:
                return -1, l, r
        print('getPalindromesCount', length, l, r, s[l:r])
        return length, l, r
    
    def longestPalindrome(self, s) -> int:
        max = 0
        maxL = -1
        maxR = -1
        for i in range(0, len(s)):
            first, l, r = self.getPalindromesCount(s, i, i)

            if first > max:
                print('first', first, l, r)
                max = first
                maxL = l
                maxR = r

            second, l, r = self.getPalindromesCount(s, i, i+1)

            if second > max:
                print('second', second, l, r)
                max = second
                maxL = l
                maxR = r


        if maxL < 0:
            maxL = 0
        # maxR = maxR if maxR < len(s) else len(s)
        print(maxL, maxR)

        return s[maxL:maxR]

inputs = [
    # ["a", "a"],
    # ["aa", "aa"],
    # ["abc", "a"],
    ["xaaa", "aaa"],
    # ["abcba", "abcba"],
    # ["abxxba", "abxxba"],
    # ["babad", "bab"],
    # ["cbbd", "bb"],
]

s = Solution()
for input in inputs:
    print(s.longestPalindrome(input[0]))
    # print(s.longestPalindrome(input[0]) == input[1])
    # print(s.isPalindrome(input[0], input[2], input[3]) == input[4])