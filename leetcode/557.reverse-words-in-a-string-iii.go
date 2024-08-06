/*
 * @lc app=leetcode id=557 lang=golang
 *
 * [557] Reverse Words in a String III
 */

 package main

import (
	"fmt"
	"strings"
)

// @lc code=start
func reverseWords(sentence string) string {
    var arr []string = strings.Split(sentence, " ")

	for i := 0; i < len(arr); i++ {
		var word string = arr[i]
		var l int = 0
		var r int = len(word)-1
		var chars = []rune(word)

		for l <= r {
			chars[l], chars[r] = chars[r], chars[l]
			r--
			l++
		}

		arr[i] = string(chars)
	}

	// fmt.Println(s.Join(arr, " "))

	return strings.Join(arr, " ")
}
// @lc code=end

func main() {
    fmt.Printf(reverseWords("Hello World from copy"))
}