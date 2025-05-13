/*
 * @lc app=leetcode id=744 lang=golang
 *
 * [744] Find Smallest Letter Greater Than Target
 */

 package main

 import (
 "fmt"
 )
 
 // @lc code=start
 func nextGreatestLetter(letters []byte, target byte) byte {
    l := 0
    r := len(letters)-1

    for l<r {
        m := (l+r)/2

        if letters[m] > target {
            r = m
        } else {
            l = m+1
        }
    }
	// fmt.Println(l,r)

    if letters[r] <= target {
        return letters[0]
    }

    return letters[l]
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
 