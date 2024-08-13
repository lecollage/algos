/*
 * @lc app=leetcode id=1351 lang=golang
 *
 * [1351] Count Negative Numbers in a Sorted Matrix
 */

 package main

 import (
 "fmt"
 )
 

// @lc code=start
func binSearch(nums []int) int {
	l := 0
	r := len(nums)-1

	for l<r {
		m := (l+r)/2

		if nums[m] < 0 {
			r = m
		} else {
			l = m+1
		}
	}

	if nums[r] >= 0 {
		return -1
	}

	return r
}

func countNegatives(grid [][]int) int {
	count := 0

	for i := 0; i < len(grid); i++ {
		row := grid[i]
		firstNegativeIndx := binSearch(row)

		if(firstNegativeIndx >= 0) {
			count += len(row)-firstNegativeIndx
		}
	}

	return count    
}
// @lc code=end



func main1() {
	tests := []struct {
		arr     [][]int
		out     int
	}{
		{[][]int{{4,3,2,-1},{3,2,1,-1},{1,1,-1,-2},{-1,-1,-2,-3}}, 8},
		{[][]int{{3,2},{1,0}}, 0},
		{[][]int{{1,-1},{-1,-1}}, 3},
	}

	for _, test := range tests {
		res := countNegatives(test.arr)
		fmt.Println(res == test.out, res)
	}
}

func main2() {
	tests := []struct {
		arr     []int
		out     int
	}{
		{[]int{4,3,2,-1}, 3},
		{[]int{3,2,1,-1}, 3},
		{[]int{1,1,-1,-2}, 2},
		{[]int{-1,-1,-2,-3}, 0},
		{[]int{1,1,2,3}, -1},
	}

	for _, test := range tests {
		res := binSearch(test.arr)
		fmt.Println(res == test.out, res)
	}
}


func main() {
	main1()
}