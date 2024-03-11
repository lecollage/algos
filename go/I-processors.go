package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"sort"
)

var inI = bufio.NewReader(os.Stdin)
var outI = bufio.NewWriter(os.Stdout)

type Processor struct {
	index  int
	energy int
}

type Task struct {
	from int
	to   int
	time int
}

var processorsCount int
var tasksCount int

var processors []Processor = make([]Processor, 0)
var tasks []Task = make([]Task, 0)

// HEAP

// An FreeProcessors is a min-heap of ints.
type FreeProcessors []int

func (h FreeProcessors) Len() int           { return len(h) }
func (h FreeProcessors) Less(i, j int) bool { return h[i] < h[j] }
func (h FreeProcessors) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *FreeProcessors) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *FreeProcessors) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

// Busy
type BusyProcessor struct {
	index int
	till  int
}

type BusyProcessors []BusyProcessor

func (h BusyProcessors) Len() int { return len(h) }
func (h BusyProcessors) Less(i, j int) bool {
	if h[i].till == h[j].till {
		return h[i].index < h[j].index
	}

	return h[i].till < h[j].till
}
func (h BusyProcessors) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *BusyProcessors) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(BusyProcessor))
}

func (h *BusyProcessors) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

/*
4 7
3 2 6 4

1 3
2 5
3 7
4 10
5 5
6 100
9 2
*/

func readHeader() {
	fmt.Fscan(inI, &processorsCount)

	fmt.Fscan(inI, &tasksCount)
}

func readProcessors() {
	for j := 0; j < processorsCount; j++ {
		var energy int

		fmt.Fscan(inI, &energy)

		//fmt.Println("word: ", word)

		processors = append(processors, Processor{
			index:  j,
			energy: energy,
		})
	}
}

func readTasks() {
	for j := 0; j < tasksCount; j++ {
		var from int
		var time int

		fmt.Fscan(inI, &from)
		fmt.Fscan(inI, &time)

		//fmt.Println("word: ", word)

		tasks = append(tasks, Task{from: from, to: from + time, time: time})
	}
}

func prepare() {
	sort.Slice(processors, func(i, j int) bool {
		return processors[i].energy < processors[j].energy
	})
}

func executeTasks() int {
	totalEnergy := 0

	free := &FreeProcessors{}
	heap.Init(free)

	for i := range processors {
		heap.Push(free, i)
	}

	//fmt.Println("free:", *free)
	//fmt.Println("INIT IS DONE")

	busy := &BusyProcessors{}
	heap.Init(busy)

	for _, task := range tasks {
		//fmt.Println()
		if len(*busy) == 0 {
			freeProcIndex := heap.Pop(free).(int)
			//fmt.Println("freeProcIndex:", freeProcIndex)
			heap.Push(busy, BusyProcessor{index: freeProcIndex, till: task.to})

			totalEnergy += task.time * processors[freeProcIndex].energy
		} else {
			// pop all that should be finished at this time
			for (*busy)[0].till <= task.from {
				proc := heap.Pop(busy).(BusyProcessor)
				heap.Push(free, proc.index)

				if len(*busy) == 0 {
					break
				}

				//fmt.Println("release proc:", proc, (*busy)[0].till, task.from, len(*busy))
			}

			if len(*free) > 0 {
				freeProcIndex := heap.Pop(free).(int)
				heap.Push(busy, BusyProcessor{index: freeProcIndex, till: task.to})

				totalEnergy += task.time * processors[freeProcIndex].energy
			} else {
				// ignore task
			}
		}

		//fmt.Println("task:", task)
		//fmt.Println("busy:", *busy, len(*busy))
		//fmt.Println("free:", *free, len(*free))
	}

	return totalEnergy
}

func main() {
	readHeader()
	readProcessors()
	readTasks()

	prepare()

	//fmt.Println("processors: ", processors)
	//fmt.Println("tasks: ", tasks)

	totalCost := executeTasks()

	//fmt.Println("processors: ", processors)
	//fmt.Println("totalCost: ", totalCost)
	//fmt.Println("busyTimes: ", busyTimes)

	//calculateCost()
	fmt.Fprintln(outI, totalCost)

	defer outI.Flush()
}
