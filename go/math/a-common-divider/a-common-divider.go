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
3
12
30
60

выходные данные
2 4 6
*/

func readInput() []int {
	var arraySize int
	array := make([]int, 0)

	fmt.Fscan(in, &arraySize)

	for i := 0; i < arraySize; i++ {
		var elem int
		fmt.Fscan(in, &elem)

		array = append(array, elem)
	}

	return array
}

func lowerLeftIndex(array []int, target int) int {
	left := -1
	right := len(array)

	for right-left > 1 {
		middle := int((right + left) / 2)

		if array[middle] < target {
			left = middle
		}

		if array[middle] >= target {
			right = middle
		}
	}

	return right + 1
}

func calculate(array []int) []int {
	minDividers := make([]int, 0)

	min := array[0]

	// find min
	for _, item := range array {
		if item < min {
			min = item
		}
	}

	// find all dividers for min
	for i := 1; i <= min; i++ {
		remainder := min % i

		if remainder == 0 {
			minDividers = append(minDividers, i)
		}
	}


	// find all commoonnDividers
	commonDividers := make(map[int]bool)
	results := make([]int, 0)

	for _, divider := range minDividers {
		isCommon := true

		for _, item := range array {
			if item != min && item%divider != 0 {
				isCommon = false
			}
		}

		if isCommon && !commonDividers[divider] {
			commonDividers[divider] = true
			results = append(results, divider)
		}
	}

	return results
}

func main() {
	// fmt.Println("START >> ")
	array := readInput()

	// fmt.Println("1 >> ", array, searchArray)

	results := calculate(array)

	for i := 0; i < len(results); i++ {
		result := results[i]
		fmt.Println(result)
	}

	defer out.Flush()
}
