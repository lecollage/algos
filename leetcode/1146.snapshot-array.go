/*
 * @lc app=leetcode id=1146 lang=golang
 *
 * [1146] Snapshot Array
 */

 package main

 import (
 "fmt"
 )
 


// @lc code=start
type SnapshotArray struct {
    currentSnapshotIndex int
	snapshots [][]int
	initialArray []int
	currentArray []int
}


func Constructor(length int) SnapshotArray {
	initialArray := make([]int, length)
	currentArray := make([]int, length)

	// copy(currentArray, initialArray)
    
	return SnapshotArray{
		currentSnapshotIndex: 0,
		snapshots: [][]int{},
		initialArray: initialArray,
		currentArray: currentArray,
	}
}


func (this *SnapshotArray) Set(index int, val int)  {
    this.currentArray[index] = val
}


func (this *SnapshotArray) Snap() int {
	arr := make([]int, len(this.currentArray))

	copy(arr, this.currentArray)
    this.snapshots = append(this.snapshots, arr)

	return len(this.snapshots)-1
}


func (this *SnapshotArray) Get(index int, snap_id int) int {
	return this.snapshots[snap_id][index]
}


/**
 * Your SnapshotArray object will be instantiated and called as such:
 * obj := Constructor(length);
 * obj.Set(index,val);
 * param_2 := obj.Snap();
 * param_3 := obj.Get(index,snap_id);
 */
// @lc code=end


func main1() {
// 	tests := []struct {
// 		arr     []int
// 		k  		int
// 		out     int
// 	}{
// 		{[]int{2,3,4,7,11}, 5, 9},
// 		{[]int{1,2,3,4}, 2, 6},
// 		{[]int{1,2}, 1, 3},
// 	}

// 	for _, test := range tests {
// 		res := findKthPositive(test.arr, test.k)
// 		fmt.Println(res == test.out, res)
// 	}

	obj := Constructor(10)
	fmt.Println(obj)

	obj.Set(1,10)
	fmt.Println(obj)

	i := obj.Snap()
	fmt.Println(i, obj)

	obj.Set(1,11)
	fmt.Println(obj)

	value := obj.Get(1,0)
	fmt.Println(value)
 }



func main() {
	main1()
}