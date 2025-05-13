/*
 * @lc app=leetcode id=118 lang=golang
 *
 * [118] Pascal's Triangle
 */

 package main

 import (
  "fmt"
 )
 
 // @lc code=start
 func getRow(rowIndex int) []int {
	 triangle := [][]int{{1}}
 
	 for i := 1; i <= rowIndex; i++ {
		 prevRow := triangle[i-1]
		 newRow := []int{1}
 
		 for j := 1; j < len(prevRow); j++ {
			 newRow = append(newRow, prevRow[j-1] + prevRow[j])
		 }
 
		 newRow = append(newRow, 1)
		 triangle = append(triangle, newRow)
	 }
 
	 // fmt.Println(triangle)
 
	 return triangle[rowIndex]
 }
 // @lc code=end
 
 func main() {
	 tests := []struct {
		 in  int
		 out []int
	 }{
		 {0, []int{}},
		 {1, []int{1}},
		 {3, []int{1,3,3,1}},
		 {4, []int{1,4,6,4,1}},
	 }
 
	 for _, test := range tests {
		 fmt.Println()
		 fmt.Println(getRow(test.in))
	 }    
 }
 