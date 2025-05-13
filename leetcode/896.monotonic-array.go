/*
 * @lc app=leetcode id=896 lang=golang
 *
 * [896] Monotonic Array
 */

package main

// @lc code=start
func isMonotonic(nums []int) bool {
	if len(nums) == 1 {
		return true
	}

	isDecreasing := nums[0] - nums[1] > 0

	for i := 0; i < len(nums)-1 ; i++ {
		isDecreasing = nums[i] - nums[i+1] > 0
		// println("isDecreasing:" ,isDecreasing, i)

		if(nums[i] != nums[i+1]) {
			break
		}
	}

	if (isDecreasing) {
		for i := 1; i < len(nums); i++ {
			if(nums[i-1] < nums[i]) {
				return false
			}
		}
	} else {
		for i := 1; i < len(nums); i++ {
			if(nums[i-1] > nums[i]) {
				return false
			}
		}
	}

    return true
}
// @lc code=end

func main() {
	tests := []struct {
		in  []int
		out bool
	}{
		{[]int{1,2,2,3}, true},
		{[]int{1,1,1,2,2,3}, true},
		{[]int{6,5,4,4}, true},
		{[]int{6,6,6,5,4,4}, true},
		{[]int{1,3,2}, false},
		{[]int{1}, true},
		{[]int{6,6}, true},
		{[]int{6,6,6}, true},
	}

	for _, test := range tests {
		println(test.out == isMonotonic(test.in))
	}    
}