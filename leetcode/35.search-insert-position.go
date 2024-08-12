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
	if(target <= nums[0]) {
		return 0
	}

	if(target > nums[len(nums)-1]) {
		return len(nums)
	}

    l := 0
	r := len(nums)-1

	for ; r-l>1; {
		m := (l+r)/2

		if(nums[m] <= target) {
			l = m
		} else {
			r = m
		}
	}

	fmt.Println(l,r)

	if(nums[l] > target) {
		return l+1
	}

	if(nums[r] > target) {
		return r+1
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
		{[]int{1,3,5,5,5,6}, 5, 6},
		{[]int{1,3,5,6}, 5, 2},
		{[]int{1,3,3,5,5,5,6}, 2, 1},
		{[]int{1,3,3,5,5,5,6}, 4, 3},
		{[]int{5,5,5}, 5, 0},
		{[]int{1,5,5,5}, 2, 1},
		{[]int{1,3,5,6}, 2, 1},
		{[]int{1,3,5,6}, 7, 4},
		{[]int{1,3,5,6}, 0, 0},
		{[]int{1,3}, 2, 1},
	}

	for _, test := range tests {
		res := searchInsert(test.arr, test.target)
		fmt.Println(res == test.out, res)
	}
}
