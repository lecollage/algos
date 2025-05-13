/*
 * @lc app=leetcode id=1539 lang=golang
 *
 * [1539] Kth Missing Positive Number
 */

 package main

 import (
 "fmt"
 )
 


// @lc code=start
func findKthPositive(arr []int, k int) int {
	num := 1
	i := 0

    for 0 < k {
		if i<len(arr) && arr[i] == num {
			num++
			i++
		} else {
			k--

			if k > 0 {
				num++
			}
		}
	}

	return num
}
// @lc code=end

func main1() {
	tests := []struct {
		arr     []int
		k  		int
		out     int
	}{
		{[]int{2,3,4,7,11}, 5, 9},
		{[]int{1,2,3,4}, 2, 6},
		{[]int{1,2}, 1, 3},
	}

	for _, test := range tests {
		res := findKthPositive(test.arr, test.k)
		fmt.Println(res == test.out, res)
	}
}

func main() {
	main1()
}