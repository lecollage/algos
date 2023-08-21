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
	tasks  []Task
}

type Task struct {
	from int
	to   int
}

var processorsCount int
var tasksCount int

var processors []Processor = make([]Processor, 0)
var tasks []Task = make([]Task, 0)

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
			tasks:  make([]Task, 0),
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

		tasks = append(tasks, Task{from: from, to: from + time})
	}
}

func sortProcessorsByEnergy() {
	sort.Slice(processors, func(i, j int) bool {
		return processors[i].energy < processors[j].energy
	})
}

func applyTasksToProcessors() int {
	totalCost := 0

	for _, task := range tasks {
	out:
		for i := 0; i < len(processors); i++ {
			if len(processors[i].tasks) == 0 {
				processors[i].tasks = make([]Task, 0)
				processors[i].tasks = append(processors[i].tasks, task)
				//fmt.Println("applyTasksToProcessors >> STEP 1 ", processors[i], task)

				totalCost += (task.to - task.from) * processors[i].energy

				break out
			} else if processors[i].tasks[len(processors[i].tasks)-1].to <= task.from {
				processors[i].tasks = append(processors[i].tasks, task)
				//fmt.Println("applyTasksToProcessors >> STEP 2 ", processors[i], task)

				totalCost += (task.to - task.from) * processors[i].energy

				break out
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

	//calculateCost()
	fmt.Fprintln(outI, totalCost)

	defer outI.Flush()
}
