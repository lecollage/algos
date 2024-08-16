/*
 * @lc app=leetcode id=153 lang=golang
 *
 * [153] Find Minimum in Rotated Sorted Array
 */


 package main

 import (
 "fmt"
 )

// @lc code=start
func findIndexOfMin(nums []int) int {
	l := 0
	r := len(nums)-1

	min := nums[0]
	minLeft := true

	if nums[len(nums)-1] < min {
		min = nums[len(nums)-1]
		minLeft = false
	}

	for l+1<r {
		m := int((l+r)/2)

		// fmt.Println(l,m,r,"min:",min)

		if minLeft {
			if nums[m] > min {
				r = m
			} else {
				l = m
			}
		} else {
			if nums[m] < min {
				r = m
			} else {
				l = m
			}
		}

		if nums[m] < min {
			min = nums[m]
			// fmt.Println("min changed to m", nums[m])
		}
	}

	// fmt.Println(l,r,"min:",min)

	if nums[r] > nums[l] {
		return l
	}

	return r
}


func findMin(nums []int) int {
    idx := findIndexOfMin(nums)

	return nums[idx]
}
// @lc code=end


func main1() {
	// MIN INDEX
	tests := []struct {
		arr     []int
		out     int
	}{
		{[]int{4,5,6,7,0,1,2}, 4},
		{[]int{2,4,5,6,7,0,1}, 5},
		{[]int{1,2,4,5,6,7,0}, 6},
		{[]int{0,1,2,4,5,6,7}, 0},
	}

	for _, test := range tests {
		res := findIndexOfMin(test.arr)
		fmt.Println(res == test.out, res)
	}
}


func main2() {
	// MIN VALUE
	tests := []struct {
		arr     []int
		out     int
	}{
		{[]int{4,5,6,7,0,1,2}, 0},
		{[]int{2,4,5,6,7,0,1}, 0},
		{[]int{1,2,4,5,6,7,0}, 0},
		{[]int{0,1,2,4,5,6,7}, 0},

		{[]int{3,4,5,1,2}, 1},
		{[]int{4,5,6,7,0,1,2}, 0},
		{[]int{11,13,15,17}, 11},
		{[]int{17,18,11,13,15,16}, 11},
	}

	for _, test := range tests {
		res := findMin(test.arr)
		fmt.Println(res == test.out, res)
	}
}


func main() {
	main1()
	main2()
}