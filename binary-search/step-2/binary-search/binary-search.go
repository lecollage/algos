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
10 10
1 61 126 217 2876 6127 39162 98126 712687 1000000000
100 6127 1 61 200 -10000 1 217 10000 1000000000

выходные данные
NO
YES
YES
YES
NO
NO
YES
YES
NO
YES
*/

func readInput() ([]int, []int) {
	var arraySize, targetsArraySize int
	array := make([]int, 0)
	targets := make([]int, 0)

	fmt.Fscan(in, &arraySize)
	fmt.Fscanln(in, &targetsArraySize)

	for i := 0; i < arraySize; i++ {
		var elem int
		fmt.Fscan(in, &elem)

		array = append(array, elem)
	}

	for i := 0; i < targetsArraySize; i++ {
		var elem int
		fmt.Fscan(in, &elem)

		targets = append(targets, elem)
	}

	return array, targets
}

func find(array []int, target int) bool {
	left := 0
	right := len(array) - 1

	for right >= left {
		middle := int((right + left) / 2)

		if array[middle] == target {
			return true
		}

		if array[middle] < target {
			left = middle + 1
		}

		if array[middle] > target {
			right = middle - 1
		}
	}

	return false
}

func calculate(array []int, targets []int) []string {
	results := make([]string, 0)

	for i := 0; i < len(targets); i++ {
		result := "NO"

		if find(array, targets[i]) {
			result = "YES"
		}

		results = append(results, result)
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
