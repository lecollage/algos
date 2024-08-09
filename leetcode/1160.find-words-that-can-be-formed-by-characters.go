/*
 * @lc app=leetcode id=1160 lang=golang
 *
 * [1160] Find Words That Can Be Formed by Characters
 */


 package main

 import (
  "fmt"
 )
 

// @lc code=start
func cloneMap(original map[string]int) map[string]int {
	clone := make(map[string]int)
	for key, value := range original {
		clone[key] = value
	}
	return clone
}

func isGood(word string, m map[string]int) bool {
	for _, rune := range word {
		key := string(rune)

		count, exists := m[key]

		if(!exists || count == 0) {
			return false
		} 

		m[key]-- 
	}

	return true
}

func countCharacters(words []string, chars string) int {
	charMap := make(map[string]int)

	for _, rune := range chars {
		key := string(rune)
	
		_, exists := charMap[key]

		if (!exists) {
			charMap[key] = 1
		} else {
			charMap[key]++
		}
	}
	
	commonLen := 0

	for _, word := range words {
		if len(word) > len(chars){
			continue
		}

		if(isGood(word, cloneMap(charMap))) {
			commonLen += len(word)
		}
	}

	// fmt.Println(commonLen, charMap)

	return commonLen
}
// @lc code=end


func main() {
	tests := []struct {
		words  []string
		chars  string
		out int
	}{
		{[]string{"cat","bt","hat","tree"}, "atach", 6},
		{[]string{"hello","world","leetcode"}, "welldonehoneyr", 10},
		{[]string{"h","world","leetcode"}, "xyz", 0},
	}

	for _, test := range tests {
		fmt.Println()
		fmt.Println(countCharacters(test.words, test.chars) == test.out)
	}    
}
