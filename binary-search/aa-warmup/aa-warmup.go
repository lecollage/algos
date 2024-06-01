package main

import (
	"bufio"
	"fmt"
	"os"
)

var in = bufio.NewReader(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

/*
Left
7 3
1 2 2 3 3 3 4

7 1
1 2 2 3 3 3 4
-> 0

7 4
1 2 2 3 3 3 4
-> 6
*/

/*
RIght
7 3
1 2 2 3 3 3 4
-> 5

7 1
1 2 2 3 3 3 4
-> 0

7 4
1 2 2 3 3 3 4
-> 6
*/

/*
Lower bound
7 5
10 20 20 30 30 30 40
-> 0

7 45
10 20 20 30 30 30 40
-> 7

7 30
10 20 20 30 30 30 40
-> 3
*/
func readInput() ([]int, int) {
	var arrayLength, searchValue int

	fmt.Fscan(in, &arrayLength)
	fmt.Fscanln(in, &searchValue)

	array := make([]int, 0)

	for arrayLength > 0 {
		var el int
		fmt.Fscan(in, &el)
		array = append(array, el)
		arrayLength--
	}

	return array, searchValue
}

func binSearchLowerBound(array []int, searchValue int) int {
	left := -1          // MinInt
	right := len(array) // MaxInt

	for left+1 < right {
		middle := int((left + right) / 2)

		if searchValue > array[middle] {
			left = middle
		} else {
			right = middle
		}
	}

	return right
}

/*
Upper bound
7 5
10 20 20 30 30 30 40
-> 0

7 45
10 20 20 30 30 30 40
-> 7

7 30
10 20 20 30 30 30 40
-> 6
*/
func binSearchUpperBound(array []int, searchValue int) int {
	left := -1
	right := len(array)

	for left+1 < right {
		middle := int((left + right) / 2)

		if searchValue >= array[middle] {
			left = middle
		} else {
			right = middle
		}
	}

	return right
}
func main() {
	array, searchValue := readInput()

	fmt.Println("input >> ", array, searchValue)

	result := binSearchUpperBound(array, searchValue)

	fmt.Println(result)

	defer out.Flush()
}
