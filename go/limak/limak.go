package main

import (
	"bufio"
	"fmt"
	"os"
)

var in = bufio.NewReader(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

/*
входные данные
3 222
выходные данные
2

4*60=240
240-222=18
5,10,15

18-5-10
*/

func readInput() (int, int) {
	var tasksCount, tripTime int

	fmt.Fscan(in, &tasksCount)
	fmt.Fscan(in, &tripTime)

	return tasksCount, tripTime
}

func calculate(tasksCount int, tripTime int) int {
	remainingTime := 240 - tripTime
	i := 0

	for ; i < tasksCount && remainingTime-((i+1)*5) >= 0; i++ {
		taskTime := (i + 1) * 5
		remainingTime -= taskTime
		// fmt.Println("1.2 >> ", remainingTime)
	}

	return i
}

func main() {
	// fmt.Println("START >> ")
	tasksCount, tripTime := readInput()

	// fmt.Println("1 >> ", tasksCount, tripTime)

	result := calculate(tasksCount, tripTime)

	fmt.Println(result)

	defer out.Flush()
}
