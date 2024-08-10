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

	for ; l+1<r; {
		m := int((l+r)/2)

		if(nums[m] <= target) {
			l = m
		} else {
			r = m
		}

		// fmt.Println(l,m,r)
	}

	if(nums[l] != target && nums[r] != target) {
		return -1
	}

	if(nums[r]==target) {
		return r
	}

	return l
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
