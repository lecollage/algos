/*
 * @lc app=leetcode id=33 lang=golang
 *
 * [33] Search in Rotated Sorted Array
 */


 package main

 import (
 "fmt"
 )
 
 
// @lc code=start
func findIndexOfMax(nums []int) int {
	l := 0
	r := len(nums)-1

	max := nums[0]

	for l+1<r {
		m := int((l+r)/2)

		// fmt.Println(l,m,r,max)

		if nums[m] < max {
			r = m
		} else {
			l = m
		}

		if nums[m] > max {
			max = nums[m]
			// fmt.Println("max changed to m", nums[m])
		}
	}

	// fmt.Println(l,r, max)

	if nums[r] > nums[l] {
		return r
	}

	return l
}

func binSearch(nums []int, target int) int {
	l := 0
	r := len(nums)-1

	for l<=r {
		m := l+(r-l)/2

		if nums[m] == target {
			return m
		}

		if nums[m] < target {
			l = m+1
		} else {
			r = m-1
		}
	}

	return -1
}


func search(nums []int, target int) int {
	indexOfMax := findIndexOfMax(nums)

	if target >= nums[0] && target <= nums[indexOfMax] {
		return binSearch(nums[:indexOfMax+1], target)
	}

	indx := binSearch(nums[indexOfMax+1:], target)

	if indx < 0 {
		return indx
	}
	
	return binSearch(nums[indexOfMax+1:], target) + indexOfMax + 1
}
// @lc code=end


func main1() {
	// MAX INDEX
	tests := []struct {
		arr     []int
		out     int
	}{
		{[]int{0,1,2,4,5,6,7}, 6},
		{[]int{7,0,1,2,4,5,6}, 0},
		{[]int{6,7,0,1,2,4,5}, 1},
		{[]int{5,6,7,0,1,2,4}, 2},
		{[]int{4,5,6,7,0,1,2}, 3},
		{[]int{2,4,5,6,7,0,1}, 4},
		{[]int{1,2,4,5,6,7,0}, 5},
	}

	for _, test := range tests {
		res := findIndexOfMax(test.arr)
		fmt.Println(res == test.out, res)
	}
}

func main2() {
	// TARGET
	tests := []struct {
		arr     []int
		target  int
		out     int
	}{
		{[]int{0,1,2,4,5,6,7}, 6, 5},
		{[]int{7,0,1,2,4,5,6}, 6, 6},
		{[]int{6,7,0,1,2,4,5}, 6, 0},
		{[]int{5,6,7,0,1,2,4}, 6, 1},
		{[]int{4,5,6,7,0,1,2}, 6, 2},
		{[]int{2,4,5,6,7,0,1}, 6, 3},
		{[]int{1,2,4,5,6,7,0}, 6, 4},

		{[]int{4,5,6,7,0,1,2}, 2, 6},

		{[]int{4,5,6,7,0,1,2}, 3, -1},
		
	}

	for _, test := range tests {
		res := search(test.arr, test.target)
		fmt.Println(res == test.out, res)
	}
}

func main3() {
	// BIN SEARCH
	tests := []struct {
		arr     []int
		target  int
		out     int
	}{
		{[]int{0,1,2,4,5,6,7}, 6, 5},
		{[]int{0,1,2,4,5,6,7}, 2, 2},
		{[]int{0,1,2,4,5,6,7}, 4, 3},
		{[]int{0,1,2,4,5,6,7}, 0, 0},
		{[]int{6,7}, 6, 0},
		{[]int{6,7}, 8, -1},
		{[]int{6,7}, 5, -1},
	}

	for _, test := range tests {
		res := binSearch(test.arr, test.target)
		fmt.Println(res == test.out, res)
	}
}



func main() {
	// main1()
	// main3()
	main2()
}