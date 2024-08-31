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
type BSTIterator struct {
	arr []int
}


func Constructor(root *TreeNode) BSTIterator {
	stack := []*TreeNode{}
	current := root
	arr := []int{}

	for current != nil || len(stack) > 0 {
		// if current != nil  {
		// 	arr = append(arr, current.Val)
		// }

		if current != nil  {
			stack = append(stack, current)
			current = current.Left
		} else {
			current = stack[len(stack)-1]
			arr = append(arr, current.Val)
			stack = stack[:len(stack)-1]
			current = current.Right
		}
	}

    return BSTIterator{
		arr: arr,
	}
}


func (this *BSTIterator) Next() int {
	ret := this.arr[0]
	this.arr = this.arr[1:]

	return ret
}


func (this *BSTIterator) HasNext() bool {
    return len(this.arr) > 0
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
				Left: nil,
				Right: nil,
			},
			Right: &TreeNode{
				Val: 6,
				Left: nil,
				Right: nil,
			},
		},
	}

	obj := Constructor(tree);

	fmt.Println(obj.Next(), obj.Next(), obj.Next(), obj.Next(), obj.Next(), obj.HasNext(), obj.Next(), obj.HasNext())
}



func main() {
	main1()
}