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
type BSTIterator struct {
    
}


func Constructor(root *TreeNode) BSTIterator {
    
}


func (this *BSTIterator) Next() int {
    
}


func (this *BSTIterator) HasNext() bool {
    
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

	obj := Constructor(root);
	param_1 := obj.Next();
	param_2 := obj.HasNext();

	fmt.Println(isValidBST(tree))
}



func main() {
	main1()
}