#
# @lc app=leetcode id=2108 lang=python3
#
# [2108] Find First Palindromic String in the Array
#

from typing import List

# @lc code=start
class Solution:
    def isPalindrome(self, word: str) -> bool:
        l = 0
        r = len(word)-1

        while r-l>=0:
            # print(l,r,word)

            if word[l] != word[r]:
                return False
            l = l+1
            r = r-1
        
        return True

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
        
        return ""

        # 2-1=1
        # 1-1=0
        
# @lc code=end

inputs = [
    [
        ["abba"], 
        "abba"
    ],
    [
        ["aba"], 
        "aba"
    ],
    [
        ["abc","car","ada","racecar","cool"],
        "ada"
    ],
    [
        ["notapalindrome","racecar"],
        "racecar"
    ],
    [
        ["def","ghi"],
        ""
    ],
    [
        ["po","zsz"],
        "zsz"
    ]
]

for [words, expected] in inputs:
    solution = Solution()
    res = solution.firstPalindrome(words)
    print(res == expected, res, words)