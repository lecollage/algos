package main

import (
"fmt"
)


// @lc code=start
type MyCircularQueue struct {
    arr []int
	head int
	tail int
}


func Constructor(k int) MyCircularQueue {
    return MyCircularQueue{
		arr: make([]int, k),
		head: 0,
		tail: 0,
	}
}


func (this *MyCircularQueue) EnQueue(value int) bool {
	// queue is full
	if this.IsFull() {
		return false
	}

	// tail is last
	if this.tail > this.head {
		this.arr[this.tail+1] = value
	}


}


// func (this *MyCircularQueue) DeQueue() bool {
    
// }


// func (this *MyCircularQueue) Front() int {
    
// }


// func (this *MyCircularQueue) Rear() int {
    
// }


// func (this *MyCircularQueue) IsEmpty() bool {
    
// }


func (this *MyCircularQueue) IsFull() bool {
    if this.head - this.tail == 1 {
		return true
	}

	if this.head == len(this.arr)-1 && this.tail == 0 {
		return true
	}

	return false
}
// @lc code=end


func main1() {
	// Your MyCircularQueue object will be instantiated and called as such:
	k := 10
	obj := Constructor(k);

	// param_1 := obj.EnQueue(value);
	// param_2 := obj.DeQueue();
	// param_3 := obj.Front();
	// param_4 := obj.Rear();
	// param_5 := obj.IsEmpty();
	// param_6 := obj.IsFull();
	
	fmt.Println(obj)
}

func main() {
	main1()
}