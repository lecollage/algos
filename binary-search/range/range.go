package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var in = bufio.NewReader(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

/*
входные данные
5
10 1 10 3 4
4
1 10
2 9
3 4
2 2

выходные данные
5 2 2 0


5
1 3 4 10 10
1
-1 2
1

5
1 3 4 10 10
1
-1 10
5

5
1 3 4 10 10
1
-2 -1
0

5
1 3 4 10 10
1
10 20

5
1 3 4 10 10
1
11 20
0

5
1 3 4 10 10
1
5 10
2
	
5
1 3 4 10 10
1
-5 10
5

5
1 3 4 10 10
1
-5 10
5

5
1 3 4 10 10
1
-5 5
3

6
-10 -3 -1 4 10 10
1
-5 -2
1

1
-1
1
5 2
1

2
3 5
1
3 5
2

4
-1000000000 3 4 1000000000
1
1000000000 1000000000
1
*/

type Range struct {
	From int
	To   int
}

func readInput() ([]int, []Range) {
	var arraySize, rangesArraySize int
	array := make([]int, 0)
	ranges := make([]Range, 0)

	// array
	fmt.Fscan(in, &arraySize)

	for i := 0; i < arraySize; i++ {
		var elem int
		fmt.Fscan(in, &elem)

		array = append(array, elem)
	}

	// fmt.Println("2 >> ", arraySize, array)

	// ranges
	fmt.Fscan(in, &rangesArraySize)

	// fmt.Println("3 >> ", rangesArraySize)

	for i := 0; i < rangesArraySize; i++ {
		var from, to int
		fmt.Fscan(in, &from)
		fmt.Fscan(in, &to)

		ranges = append(ranges, Range{From: from, To: to})
	}

	// fmt.Println("4 >> ", ranges)

	return array, ranges
}

func getLeftIndex(array []int, target int) int {
	left := -1
	right := len(array)

	if array[0] == target {
		return 0
	}

	for right-left > 1 {
		middle := int((right + left) / 2)

		if left > -1 && array[left] == target {
			return left
		}

		if array[middle] == target {
			return middle
		}

		if array[middle] < target {
			left = middle
		}

		if array[middle] > target {
			right = middle
		}
	}

	return left + 1
}

func getRightIndex(array []int, target int) int {
	left := -1
	right := len(array)

	if array[len(array)-1] == target {
		return len(array) - 1
	}

	for right-left > 1 {
		middle := int((right + left) / 2)

		if right < len(array) && array[right] == target {
			return right
		}

		if array[middle] == target {
			return middle
		}

		if array[middle] < target {
			left = middle
		}

		if array[middle] > target {
			right = middle
		}
	}

	return right - 1
}

func howManyNumbersInRange(array []int, from int, to int) int {
	// find the left max index with from
	// find the right min index with to
	// return the difference between indexes

	leftIndex := getLeftIndex(array, from)
	rightIndex := getRightIndex(array, to)

	// fmt.Println("5 >> ", leftIndex, rightIndex)

	if leftIndex > rightIndex {
		return 0
	}

	return rightIndex - leftIndex + 1
}

func calculate(array []int, ranges []Range) []int {
	sort.Slice(array, func(i, j int) bool {
		return array[i] < array[j]
	})

	// fmt.Println("6 >> ", array)

	results := make([]int, 0)

	for i := 0; i < len(ranges); i++ {
		curr := ranges[i]
		results = append(results, howManyNumbersInRange(array, curr.From, curr.To))
	}

	return results
}

func main() {
	// fmt.Println("START >> ")
	array, ranges := readInput()

	// fmt.Println("1 >> ", array, searchArray)

	results := calculate(array, ranges)

	for i := 0; i < len(results); i++ {
		result := results[i]
		fmt.Print(result, " ")
	}

	defer out.Flush()
}
