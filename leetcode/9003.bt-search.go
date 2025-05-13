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
func getArr(root *TreeNode) []int {
	stack := []*TreeNode{}
	arr := []int{}

	if root == nil {
		return []int{}
	}

	stack = append(stack, root)

	for len(stack) > 0 {
		current := stack[len(stack) - 1]
		arr = append(arr, current.Val)

		stack = stack[:len(stack) - 1]

		if current.Right != nil {
			stack = append(stack, current.Right)
		}

		if current.Left != nil {
			stack = append(stack, current.Left)
		}
	}

	return arr
}

func searchBST(root *TreeNode, val int) *TreeNode {
	stack := []*TreeNode{}
	current := root

	for current != nil || len(stack) > 0 {
		if current != nil  {
			stack = append(stack, current)
			current = current.Left
		} else {
			current = stack[len(stack)-1]

			if current.Val == val {
				return current
			}

			stack = stack[:len(stack)-1]
			current = current.Right
		}
	}

	return nil
}
// @lc code=end


func main1() {
	tree := &TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 4,
				Left: nil,
				Right: nil,
			},
			Right: nil,
		},
		Right: &TreeNode{
			Val: 3,
			Left: &TreeNode{
				Val: 5,
				Left: &TreeNode{
					Val: 7,
					Left: nil,
					Right: nil,
				},
				Right: &TreeNode{
					Val: 7,
					Left: nil,
					Right: nil,
				},
			},
			Right: &TreeNode{
				Val: 6,
				Left: nil,
				Right: nil,
			},
		},
	}

	fmt.Println(searchBST(tree, 3))
}



func main() {
	main1()
}