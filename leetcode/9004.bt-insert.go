package main

import (
"fmt"
)



type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func insertIntoBST(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return &TreeNode{
			Val: val,
			Left: nil,
 			Right: nil,
		}
	}

	if val > root.Val {
		root.Right = insertIntoBST(root.Right, val)
		return root
	}
	
	root.Left = insertIntoBST(root.Left, val)
	return root
}
// @lc code=end


func main1() {
	tree := &TreeNode{
		Val: 4,
		Left: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 1,
				Left: nil,
				Right: nil,
			},
			Right: &TreeNode{
				Val: 3,
				Left: nil,
				Right: nil,
			},
		},
		Right: &TreeNode{
			Val: 7,
			Left: nil,
			Right: nil,
		},
	}

	// tree := &TreeNode{
	// 	Val: 4,
	// 	Left: nil,
	// 	Right: nil,
	// }

	newTree := insertIntoBST(tree, 5)

	fmt.Println(newTree.Val, newTree.Left.Val, newTree.Right.Val, newTree.Right.Left.Val)
}



func main() {
	main1()
}