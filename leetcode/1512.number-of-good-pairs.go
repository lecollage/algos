/*
 * @lc app=leetcode id=1512 lang=golang
 *
 * [1512] Number of Good Pairs
 */

package main


// import (
	// "fmt"
// )

// @lc code=start
func numIdenticalPairs(nums []int) int {
	dict := make(map[int]int)
	pairs := 0

	for i := 0; i < len(nums); i++ {
		value, found := dict[nums[i]]

		if(found) {
			pairs += value
			dict[nums[i]] += 1
		} else {
			dict[nums[i]] = 1
		}
	}

	// fmt.Println("dict:", dict)

	return pairs
}
// @lc code=end

/*
1:1 0
1:2 1
1:3 3
1:4 6
*/

func main() {
	tests := []struct {
		in  []int
		out int
	}{
		{[]int{1,2,3,1,1,3}, 4},
		{[]int{1,1,1,1}, 6},
		{[]int{1,2,3}, 0},
	}

	for _, test := range tests {
		println(test.out == numIdenticalPairs(test.in))
	}    
}