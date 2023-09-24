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
	var arraySize, searchArraySize int
	array := make([]int, 0)
	searchArray := make([]int, 0)

	fmt.Fscan(in, &arraySize)
	fmt.Fscanln(in, &searchArraySize)

	for i := 0; i < arraySize; i++ {
		var elem int
		fmt.Fscan(in, &elem)

		array = append(array, elem)
	}

	for i := 0; i < searchArraySize; i++ {
		var elem int
		fmt.Fscan(in, &elem)

		searchArray = append(searchArray, elem)
	}

	return array, searchArray
}

func find(array []int, search int) bool {
	left := 0
	right := len(array) - 1

	for right >= left {
		middle := int((right + left) / 2)

		if array[middle] == search {
			return true
		}

		if array[middle] < search {
			left = middle + 1
		}

		if array[middle] > search {
			right = middle - 1
		}
	}

	return false
}

func calculate(array []int, searchArray []int) []string {
	results := make([]string, 0)

	for i := 0; i < len(searchArray); i++ {
		result := "NO"

		if find(array, searchArray[i]) {
			result = "YES"
		}

		results = append(results, result)
	}

	return results
}

func main() {
	// fmt.Println("START >> ")
	array, searchArray := readInput()

	// fmt.Println("1 >> ", array, searchArray)

	results := calculate(array, searchArray)

	for i := 0; i < len(results); i++ {
		result := results[i]
		fmt.Println(result)
	}

	defer out.Flush()
}
