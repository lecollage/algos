/*
 * @lc app=leetcode id=844 lang=golang
 *
 * [844] Backspace String Compare
 */

package main

import (
	"fmt"
)

// @lc code=start
func getString(s string) string {
	var stack []rune
	
	for _, rune := range s {
		if(rune == '#') {
			if(len(stack) > 0) {
				stack = stack[:len(stack)-1]
			}
		} else {
			stack = append(stack, rune)
		}
	}

	return string(stack)
}

func backspaceCompare(s string, t string) bool {
	// fmt.Println(getString(s), getString(t))

	return getString(s) == getString(t)
}
// @lc code=end

func main() {
	tests := []struct {
		s   string
		t   string
		out bool
	}{
		// {"ab#c", "ad#c", true},
		// {"ab##", "c#d#", true},
		// {"a#c", "b", false},
		{"a#c", "", false},
	}

	for _, test := range tests {
		fmt.Println(test.out == backspaceCompare(test.s, test.t))
	}    
}
