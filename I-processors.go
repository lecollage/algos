package main

import (
	"bufio"
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

var busyTimes = make([]int, 0)

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

	busyTimes = make([]int, processorsCount)

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

func sortProcessorsByEnergy() {
	sort.Slice(processors, func(i, j int) bool {
		return processors[i].energy < processors[j].energy
	})

	for i := 0; i < processorsCount; i++ {
		busyTimes[i] = 0
	}
}

func applyTasksToProcessors() int {
	totalCost := 0

	for _, task := range tasks {
		for i := 0; i < processorsCount; i++ {
			if busyTimes[i] <= task.from {
				busyTimes[i] = task.to
				totalCost += task.time * processors[i].energy
				break
			}
		}
	}

	return totalCost
}

func main() {
	readHeader()
	readProcessors()
	readTasks()

	sortProcessorsByEnergy()

	//fmt.Println("processors: ", processors)
	//fmt.Println("tasks: ", tasks)

	totalCost := applyTasksToProcessors()

	//fmt.Println("processors: ", processors)
	//fmt.Println("totalCost: ", totalCost)
	//fmt.Println("busyTimes: ", busyTimes)

	//calculateCost()
	fmt.Fprintln(outI, totalCost)

	defer outI.Flush()
}
