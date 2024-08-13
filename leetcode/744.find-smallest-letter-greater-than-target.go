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
func nextGreatestLetter(nums []byte, target byte) byte {
	if(nums[0]>target) {
		return nums[0]
	}

	if(nums[len(nums)-1]<=target) {
		return nums[0]
	}

	l:=0
	r:=len(nums)-1

	for l<r {
		m := (l+r)/2

		if(nums[m] <= target) {
			l = m+1
		} else {
			r = m
		}
	}

	// fmt.Println(l,r)

	return nums[l]
}
 // @lc code=end
 
 
 func main() {
	 tests := []struct {
		 arr     []byte
		 target  byte
		 out     byte
	 }{
		 {[]byte{'c','f','j'}, 'a', 'c'},
		 {[]byte{'c','f','j'}, 'c', 'f'},
		 {[]byte{'c','f','j'}, 'j', 'c'},
		 {[]byte{'x','x','y','y'}, 'z', 'x'},
	}
 
	 for _, test := range tests {
		 res := nextGreatestLetter(test.arr, test.target)
		 fmt.Println(res == test.out, string(res))
	 }
 }
 