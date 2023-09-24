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
5 5
3 3 5 8 9
2 4 8 1 10

выходные данные
0
2
4
0
5
*/

func readInput() ([]int, []int) {
	var arraySize, targetArraySize int
	array := make([]int, 0)
	targets := make([]int, 0)

	fmt.Fscan(in, &arraySize)
	fmt.Fscanln(in, &targetArraySize)

	for i := 0; i < arraySize; i++ {
		var elem int
		fmt.Fscan(in, &elem)

		array = append(array, elem)
	}

	for i := 0; i < targetArraySize; i++ {
		var elem int
		fmt.Fscan(in, &elem)

		targets = append(targets, elem)
	}

	return array, targets
}

func upperRightIndex(array []int, target int) int {
	left := -1
	right := len(array)

	for right-left > 1 {
		middle := int((right + left) / 2)

		if array[middle] <= target {
			left = middle
		}

		if array[middle] > target {
			right = middle
		}
	}

	return left + 1
}

func calculate(array []int, targets []int) []int {
	results := make([]int, 0)

	for i := 0; i < len(targets); i++ {
		results = append(results, upperRightIndex(array, targets[i]))
	}

	return results
}

func main() {
	// fmt.Println("START >> ")
	array, targets := readInput()

	// fmt.Println("1 >> ", array, searchArray)

	results := calculate(array, targets)

	for i := 0; i < len(results); i++ {
		result := results[i]
		fmt.Println(result)
	}

	defer out.Flush()
}
