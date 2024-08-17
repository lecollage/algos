/*
 * @lc app=leetcode id=34 lang=golang
 *
 * [34] Find First and Last Position of Element in Sorted Array
 */


 package main

 import (
 "fmt"
 )
 

// @lc code=start
func lowerBound(nums []int, target int) int {
	l:=0
	r:=len(nums)-1

	for l+1<r {
		m:=l+(r-l)/2

		if nums[m] < target {
			l = m
		} else {
			r = m
		}
	}

	// fmt.Println(l,r)

	if nums[l] == target {
		return l
	}

	if nums[r] == target {
		return r
	}

	return -1
}

func upperBound(nums []int, target int) int {
	l:=0
	r:=len(nums)-1

	for l+1<r {
		m:=l+(r-l)/2

		if nums[m] <= target {
			l = m
		} else {
			r = m
		}
	}

	// fmt.Println(l,r)

	if nums[r] == target {
		return r
	}

	if nums[l] == target {
		return l
	}

	return -1
}

func searchRange(nums []int, target int) []int {
	if len(nums) == 0 {
		return []int{-1,-1}
	}

    return []int{lowerBound(nums, target), upperBound(nums, target)}
}
// @lc code=end


func main1() {
	// LOWER BOUND
	tests := []struct {
		arr     []int
		target  int
		out     int
	}{
		{[]int{0,1,2,2,2,4,5,6,7}, 2, 2},
		{[]int{0,1,2,2,2,4,5,5,5,6,7}, 5, 6},
		{[]int{0,0,0,1,2,2,2,4,5,5,5,6,7}, 0, 0},
		{[]int{0,1,2,3,4,5,6,7,7,7}, 7, 7},
		{[]int{0,1,2,3,4,5,6,7,7,7}, 8, -1},
		{[]int{1,2,3,4,5,6,7,7,7}, 0, -1},
	}

	for _, test := range tests {
		res := lowerBound(test.arr, test.target)
		fmt.Println(res == test.out, res)
	}
}

func main2() {
	// UPPER BOUND
	tests := []struct {
		arr     []int
		target  int
		out     int
	}{
		{[]int{0,1,2,2,2,4,5,6,7}, 2, 4},
		{[]int{0,1,2,2,2,4,5,5,5,6,7}, 5, 8},
		{[]int{0,0,0,1,2,2,2,4,5,5,5,6,7}, 0, 2},
		{[]int{0,1,2,3,4,5,6,7,7,7}, 7, 9},
		{[]int{0,1,2,3,4,5,6,7,7,7}, 8, -1},
		{[]int{1,2,3,4,5,6,7,7,7}, 0, -1},
	}

	for _, test := range tests {
		res := upperBound(test.arr, test.target)
		fmt.Println(res == test.out, res)
	}
}

func main3() {
	// RANGE
	tests := []struct {
		arr     []int
		target  int
		out     []int
	}{
		{[]int{0,1,2,2,2,4,5,6,7}, 2, []int{2, 4}},
		{[]int{0,1,2,2,2,4,5,5,5,6,7}, 5, []int{6, 8}},
		{[]int{0,0,0,1,2,2,2,4,5,5,5,6,7}, 0, []int{0, 2}},
		{[]int{0,1,2,3,4,5,6,7,7,7}, 7, []int{7, 9}},

		{[]int{0,1,2,3,4,5,6,7,7,7}, 8, []int{-1, -1}},
		{[]int{1,2,3,4,5,6,7,7,7}, 0, []int{-1, -1}},
		
		{[]int{}, 0, []int{-1, -1}},
		{[]int{1}, 1, []int{0, 0}},
		{[]int{1,1}, 1, []int{0, 1}},
	}

	for _, test := range tests {
		res := searchRange(test.arr, test.target)
		fmt.Println(res[0] == test.out[0] && res[1] == test.out[1], res)
	}
}

func main() {
	// main1()
	// main2()
	main3()
}