/*
 * @lc app=leetcode id=278 lang=golang
 *
 * [278] First Bad Version
 */
 package main


 import (
	"fmt"
	// "math"
	)
	
	
	
	

// @lc code=start
/** 
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad 
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */

func isBadVersion(version int) bool {
	if version >= 1 {
		return true
	}

	return false
}

func firstBadVersion(n int) int {

	l := 1
	r := n

	for l<r {
		m := l + (r-l)/2

		if isBadVersion(m) == true {
			r = m
		} else {
			l = m+1
		}
	}
    
	// fmt.Println(l,r)

	return l
}
// @lc code=end




func main1() {
	tests := []struct {
		in     int
	}{
		{5},
	}

	for _, test := range tests {
		res := firstBadVersion(test.in)
		fmt.Println(res)
	}
}

func main() {
	main1()
}