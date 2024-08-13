/*
 * @lc app=leetcode id=704 lang=golang
 *
 * [704] Binary Search
 */

package main

import (
"fmt"
)

// @lc code=start
func search(nums []int, target int) int {
	l := 0
	r := len(nums)-1

	for l<=r {
		m := (l+r)/2

		switch {
		case nums[m] < target:
			l = m+1
		case nums[m] > target:
			r = m-1
		default: 
			return m
		}
	}

	return -1
}
// @lc code=end

func main() {
	tests := []struct {
		arr     []int
		target  int
		out     int
	}{
		{[]int{-1,0,3,5,9,12}, 9, 4},
		{[]int{-1,0,3,5,9,12}, -1, 0},
		{[]int{-1,0,3,5,9,12}, 0, 1},
		{[]int{-1,0,3,5,9,12}, 12, 5},
		{[]int{-1,0,3,5,9,12}, 2, -1},
	}

	for _, test := range tests {
		res := search(test.arr, test.target)
		fmt.Println(res == test.out, res)
	}
}
