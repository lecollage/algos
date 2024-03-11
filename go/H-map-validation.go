package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var out = bufio.NewWriter(os.Stdout)

var visited []string
var colorIslands map[string]int

func readMatrix(in *bufio.Reader) [][]string {
	// read set
	/*
		3 7
		R.R.R.G
		.Y.G.G.
		B.Y.V.V
	*/

	// read matrix description
	var rowsCount, columnsCount int
	fmt.Fscan(in, &rowsCount, &columnsCount)

	//fmt.Fprintln(out, rowsCount, columnsCount)

	// read matrix
	var matrix = make([][]string, rowsCount)

	for i := 0; i < rowsCount; i++ {
		matrix[i] = make([]string, columnsCount)
		var rawRow string
		fmt.Fscan(in, &rawRow)

		var row = strings.Split(rawRow, "")
		for j := 0; j < columnsCount; j++ {
			matrix[i][j] = row[j]
		}
	}

	return matrix
}

func validateMap() {
	in := bufio.NewReader(os.Stdin)

	var setsCount int

	fmt.Fscan(in, &setsCount)

	for i := 0; i < setsCount; i++ {
		var matrix = readMatrix(in)

		//fmt.Fprintln(out, matrix)

		visited = make([]string, 0)
		colorIslands = make(map[string]int)

		var isCorrect = isMatrixCorrect(matrix)

		if isCorrect {
			fmt.Fprintln(out, "YES")
		} else {
			fmt.Fprintln(out, "NO")
		}
	}
}

func contains[T comparable](s []T, e T) bool {
	for _, v := range s {
		if v == e {
			return true
		}
	}
	return false
}

func isMatrixCorrect(matrix [][]string) bool {
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			var element = matrix[i][j]
			elementIndex := fmt.Sprintf("%d:%d", i, j)

			//fmt.Fprintln(out, "isMatrixCorrect >> START >> ", element, i, j)

			if element != "." && !contains(visited, elementIndex) {
				_, ok := colorIslands[element]

				if !ok {
					colorIslands[element] = 0
				}

				exploreColor(matrix, i, j)

				colorIslands[element]++

				//fmt.Fprintln(out, "isMatrixCorrect >> STEP 1 >> colorIslands: ", colorIslands)

				if colorIslands[element] > 1 {
					return false
				}
			}
		}
	}

	return true
}

/*
queue := make([]int, 0)

// Push to the queue
queue = append(queue, 1)

// Top (just get next element, don't remove it)
x = queue[0]

// Discard top element
queue = queue[1:]

// Is empty ?
if len(queue) == 0 {
	fmt.Println("Queue is empty !")
}
*/

/*
	i, j - 2
	i, j + 2
	i - 1, j - 1
	i + 1, j - 1
	i - 1, j + 1
	i + 1, j + 1
*/

type QueueItem struct {
	i int
	j int
}

func exploreColor(matrix [][]string, i int, j int) {
	color := matrix[i][j]

	queue := make([]QueueItem, 0)
	item := QueueItem{i: i, j: j}

	queue = append(queue, item)

	//fmt.Fprintln(out, queue)

	for len(queue) > 0 {
		item := queue[0]
		//fmt.Fprintln(out, "queue: ", queue)

		queue = queue[1:]

		element := "."

		if item.i >= 0 && item.j >= 0 && item.i < len(matrix) && item.j < len(matrix[item.i]) {
			element = matrix[item.i][item.j]
		}

		elementIndex := fmt.Sprintf("%d:%d", item.i, item.j)

		if element != "." && !contains(visited, elementIndex) && color == element {
			queue = append(queue, QueueItem{item.i, item.j - 2})
			queue = append(queue, QueueItem{item.i, item.j + 2})
			queue = append(queue, QueueItem{item.i - 1, item.j - 1})
			queue = append(queue, QueueItem{item.i + 1, item.j - 1})
			queue = append(queue, QueueItem{item.i - 1, item.j + 1})
			queue = append(queue, QueueItem{item.i + 1, item.j + 1})

			if !contains(visited, elementIndex) {
				visited = append(visited, elementIndex)
			}

			//fmt.Fprintln(out, "exploreColor >> visited", visited, color, element)
		}
	}
}

func main() {
	validateMap()

	defer out.Flush()
}
