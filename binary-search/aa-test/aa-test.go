/*
ввод
6
1 4 6 8 9 10
5
3 2 8 4 0

вывод
-1 -1 3 1 -1
*/

package main

import (
	"bufio"
	"fmt"
	"os"
)

var in = bufio.NewReader(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

/*
6
1 4 6 8 9 10
5
3 2 8 4 0

6
1 4 6 8 9 10
4
-3 1 10 20
*/
func readInput() ([]int, []int) {
	var arrayLength int

	fmt.Fscan(in, &arrayLength)

	array := make([]int, 0)

	for i := 0; i < arrayLength; i++ {
		var elem int
		fmt.Fscan(in, &elem)

		array = append(array, elem)
	}

	var searchArrayLength int

	fmt.Fscan(in, &searchArrayLength)

	searchArray := make([]int, 0)

	for i := 0; i < searchArrayLength; i++ {
		var elem int
		fmt.Fscan(in, &elem)

		searchArray = append(searchArray, elem)
	}

	return array, searchArray
}

/*
1 4 6 8 9 10
left: 0
right: 6
middle: 3


left+1 < right
left < right

6
1 4 4 8 8 10
4
-3 1 10 20

6
1 4 4 8 8 10
1
-3

 -> -1 0 5 -1

7
1 4 4 8 8 8 10
2
4 8
*/

func binSearch(array []int, searchItem int) int {
	left := -1
	right := len(array)

	for left+1 < right {
		middle := int((left + (right - left) / 2))

		if searchItem >= array[middle] {
			left = middle
		} else {
			right = middle
		}
	}

	if left != -1 && array[left] == searchItem {
		return left
	}

	return -1
}

func main() {
	// fmt.Println("START >> ")
	array, searchArray := readInput()

	fmt.Println("1 >> ", array, searchArray)

	for _, searchItem := range searchArray {
		fmt.Println(binSearch(array, searchItem))
	}

	defer out.Flush()
}
