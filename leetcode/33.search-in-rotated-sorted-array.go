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

		fmt.Println(l,m,r,max)

		if nums[m] < max {
			r = m
		} else {
			l = m
		}

		if nums[m] > max {
			max = nums[m]
			fmt.Println("max changed to m", nums[m])
		}
	}

	fmt.Println(l,r, max)

	if nums[r] > nums[l] {
		return r
	}

	return l
}

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

		fmt.Println(l,m,r,"min:",min)

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
			fmt.Println("min changed to m", nums[m])
		}
	}

	fmt.Println(l,r,"min:",min)

	if nums[r] > nums[l] {
		return l
	}

	return r
}


func search(nums []int, target int) int {
    return 1
}
// @lc code=end




func main1() {
	// MAX 

	tests := []struct {
		arr     []int
		out     int
	}{
		// {[]int{4,5,6,7,0,1,2}, 4},
		{[]int{2,4,5,6,7,0,1}, 4},
		// {[]int{1,2,4,5,6,7,0}, 5},
		// {[]int{0,1,2,4,5,6,7}, 6},
	}

	for _, test := range tests {
		res := findIndexOfMax(test.arr)
		fmt.Println(res == test.out, res)
	}
}

func main2() {
	// MIN 

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


func main() {
	// main1()
	main2()
}