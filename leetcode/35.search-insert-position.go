/*
 * @lc app=leetcode id=35 lang=golang
 *
 * [35] Search Insert Position
 */

package main

import (
"fmt"
)

// @lc code=start
func searchInsert(nums []int, target int) int {
	l := 0
	r := len(nums)-1

	for l<=r {
		m := int((l+r)/2)

		switch{
		case nums[m] < target:
			l = m+1
		case nums[m] > target:
			r = m-1
		default: 
			return m
		}
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
		{[]int{1,3,5,5,5,6}, 5, 2},
		{[]int{1,3,5,6}, 5, 2},
		// {[]int{1,3,3,5,5,5,6}, 2, 1},
		// {[]int{1,3,3,5,5,5,6}, 4, 3},
		// {[]int{5,5,5}, 5, 0},
		// {[]int{1,5,5,5}, 2, 1},
		// {[]int{1,3,5,6}, 2, 1},
		// {[]int{1,3,5,6}, 7, 4},
		// {[]int{1,3,5,6}, 0, 0},
		// {[]int{1,3}, 2, 1},
	}

	for _, test := range tests {
		res := searchInsert(test.arr, test.target)
		fmt.Println(res == test.out, res)
	}
}
