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
type NodesPair struct {
	parent *TreeNode
	node *TreeNode
	direction string 
}

func findNode(root *TreeNode, key int) NodesPair {
	stack := []*TreeNode{}

	if root.Val == key {
		return NodesPair{
			parent: nil,
			node: root,		
			direction: "",
		}
	}

	stack = append(stack, root)

	for len(stack) > 0 {
		current := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		
		if current.Right != nil {
			if current.Right.Val == key {
				return NodesPair{
					parent: current,
					node: current.Right,		
					direction: "Right",
				}
			}

			stack = append(stack, current.Right)
		}

		if current.Left != nil {
			if current.Left.Val == key {
				return NodesPair{
					parent: current,
					node: current.Left,		
					direction: "Left",
				}
			}

			stack = append(stack, current.Left)
		}
	}

	return NodesPair{
		parent: nil,
		node: nil,
		direction: "",
	}
}

func findLeftMostNode(root *TreeNode) NodesPair {
	if root.Left == nil {
		return NodesPair{
			parent: nil,
			node: root,
			direction: "",
		}
	}

	stack := []*TreeNode{}

	stack = append(stack, root)

	for len(stack) > 0 {
		current := stack[len(stack)-1]

		stack = stack[:len(stack)-1]

		if current.Left != nil {
			if current.Left.Left == nil {
				return NodesPair {
					parent: current,
					node: current.Left,
					direction: "",
				}
			}

			stack = append(stack, current.Left)
		} 
	}

	return NodesPair{
		parent: nil,
		node: nil,
		direction: "",
	}
}
 
func deleteNode(root *TreeNode, key int) *TreeNode {
	if root == nil {
		return nil
	}

	if root.Val == key && root.Left == nil && root.Right == nil {
		return nil
	}

	pair := findNode(root, key)

	// Case 1: not found
	if pair.parent == nil && pair.node == nil {
		return root
	}

	node := pair.node
	parent := pair.parent
	direction := pair.direction

	// Case 2: no left and no right
	if node.Left == nil && node.Right == nil {
		if direction == "Right" {
			parent.Right = nil
		}

		if direction == "Left" {
			parent.Left = nil
		}

		return root
	}

	// Case 3: One child, Right only
	if node.Left == nil && node.Right != nil {
		if direction == "Right" {
			parent.Right = node.Right
		}

		if direction == "Left" {
			parent.Left = node.Right
		}

		return root
	}

	// Case 3: One child, Left only
	if node.Left != nil && node.Right == nil {
		if direction == "Right" {
			parent.Right = node.Left
		}

		if direction == "Left" {
			parent.Left = node.Left
		}

		return root
	}

	// Case 4: Two children
	nodes := findLeftMostNode(node.Right)

	node.Val = nodes.node.Val
	
	if nodes.parent != nil {
		nodes.parent.Left = nil	
	} else {
		node.Right = nil
	}

	return root
}
// @lc code=end


func main1() {
	// tree := &TreeNode{
	// 	Val: 5,
	// 	Left: &TreeNode{
	// 		Val: 3,
	// 		Left: &TreeNode{
	// 			Val: 2,
	// 			Left: nil,
	// 			Right: nil,
	// 		},
	// 		Right: &TreeNode{
	// 			Val: 4,
	// 			Left: nil,
	// 			Right: nil,
	// 		},
	// 	},
	// 	Right: &TreeNode{
	// 		Val: 6,
	// 		Left: nil,
	// 		Right: &TreeNode{
	// 			Val: 7,
	// 			Left: nil,
	// 			Right: nil,
	// 		},
	// 	},
	// }

	// var tree *TreeNode = nil
	
	
	tree := &TreeNode{
		Val: 0,
		Left: nil,
		Right: nil,
	}

	// nodes := findNode(tree, 3)
	// if nodes.parent != nil && nodes.node != nil {
	// 	fmt.Println(nodes.node.Val, nodes.parent.Val)
	// } else if nodes.node != nil {
	// 	fmt.Println(nodes.node.Val, nil)
	// } else {
	// 	fmt.Println(nil)
	// }

	tree = deleteNode(tree, 0)
	fmt.Println(tree)
}

func main() {
	main1()
}