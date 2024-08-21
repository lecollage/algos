package main

import (
"fmt"
"math"
)



type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

// @lc code=start
func isValidBSTInner(root *TreeNode, min int, max int) bool {
	if root == nil {	
		return true
	}

	if root.Val <= min || root.Val >= max {
		return false
	}

	return isValidBSTInner(root.Left, min, root.Val) && isValidBSTInner(root.Right, root.Val, max)
}

func isValidBST(root *TreeNode) bool {
	return isValidBSTInner(root.Left, math.MinInt, root.Val) && 
		isValidBSTInner(root.Right, root.Val, math.MaxInt)

}
// @lc code=end


func main1() {
	tree := &TreeNode{
		Val: 1,
		Left: nil,
		Right: &TreeNode{
			Val: 1,
			Right: nil,
			Left: nil,
		},
	}

	fmt.Println(isValidBST(tree))
}



func main() {
	main1()
}