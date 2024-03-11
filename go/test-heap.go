// // This example demonstrates an integer heap built using the heap interface.
package main

//
//import (
//	"container/heap"
//	"fmt"
//)
//
//// An FreeProcessors is a min-heap of ints.
//type FreeProcessors []int
//
//func (h FreeProcessors) Len() int           { return len(h) }
//func (h FreeProcessors) Less(i, j int) bool { return h[i] < h[j] }
//func (h FreeProcessors) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
//
//func (h *FreeProcessors) Push(x any) {
//	// Push and Pop use pointer receivers because they modify the slice's length,
//	// not just its contents.
//	*h = append(*h, x.(int))
//}
//
//func (h *FreeProcessors) Pop() any {
//	old := *h
//	n := len(old)
//	x := old[n-1]
//	*h = old[0 : n-1]
//	return x
//}
//
//// Busy
//type BusyProcessor struct {
//	index     int
//	procIndex int
//	till      int
//}
//
//type BusyProcessors []BusyProcessor
//
//func (h BusyProcessors) Len() int { return len(h) }
//func (h BusyProcessors) Less(i, j int) bool {
//	fmt.Println("Less >> i, j: ", i, j, h[i], h[j])
//
//	if h[i].till == h[j].till {
//		return h[i].procIndex < h[j].procIndex
//	}
//
//	return h[i].till < h[j].till
//}
//func (h BusyProcessors) Swap(i, j int) {
//	h[i], h[j] = h[j], h[i]
//	h[i].index = i
//	h[j].index = j
//}
//
//func (pq *BusyProcessors) Push(x any) {
//	n := len(*pq)
//	item := x.(BusyProcessor)
//	item.index = n
//	*pq = append(*pq, item)
//}
//
//func (pq *BusyProcessors) Pop() any {
//	old := *pq
//	n := len(old)
//	item := old[n-1]
//	//old[n-1] = nil  // avoid memory leak
//	item.index = -1 // for safety
//	*pq = old[0 : n-1]
//	return item
//}
//
//// This example inserts several ints into an FreeProcessors, checks the minimum,
//// and removes them in order of priority.
//func main() {
//	//free := &FreeProcessors{1, 0, 2}
//	//heap.Init(free)
//	//fmt.Println("init 0: %d\n", (*free)[0])
//	//
//	//heap.Push(free, 3)
//	//
//	//fmt.Println("free: ", free)
//	//
//	//popped := heap.Pop(free).(int)
//	//
//	//fmt.Printf("popped: %d\n", popped)
//	//for free.Len() > 0 {
//	//	fmt.Printf("%d ", heap.Pop(free))
//	//}
//
//	// busy
//	busy := &BusyProcessors{}
//	heap.Init(busy)
//
//	heap.Push(busy, BusyProcessor{procIndex: 2, till: 10})
//	heap.Push(busy, BusyProcessor{procIndex: 1, till: 7})
//	heap.Push(busy, BusyProcessor{procIndex: 0, till: 14})
//	heap.Push(busy, BusyProcessor{procIndex: 3, till: 10})
//
//	fmt.Println("busy:", *busy)
//}
