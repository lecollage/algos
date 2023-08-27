package main

import (
	"fmt"
	"strconv"
	"strings"
)

type Matrix [][]int

const WATER = 1
const LAND = 0

type ItemX struct {
	i int
	j int
}

var visitedX = make(map[string]bool)

func buildKey(i int, j int) string {
	return fmt.Sprintf("%d:%d", i, j)
}

func parseKey(key string) (int, int) {
	strs := strings.Split(key, ":")
	i, _ := strconv.Atoi(strs[0])
	j, _ := strconv.Atoi(strs[1])

	return i, j
}

func isVisited(i int, j int) bool {
	key := buildKey(i, j)
	_, ok := visitedX[key]

	return ok
}

func visit(i int, j int) {
	key := buildKey(i, j)
	visitedX[key] = true
}

func explore(matrix *Matrix, startI int, startJ int) int {
	length := 0

	// fmt.Println("explore START >> ", startI, startJ)

	queue := make([]ItemX, 0)

	queue = append(queue, ItemX{i: startI, j: startJ})

	for len(queue) > 0 {
		fmt.Println("explore >> queue: ", queue)

		currentQueueItem := queue[0]
		queue = queue[1:]

		i := currentQueueItem.i
		j := currentQueueItem.j
		matrixLen := len(*matrix)
		rowLen := len((*matrix)[i])
		currentItem := (*matrix)[i][j]

		if currentItem == WATER && !isVisited(i, j) {
			length++
			visit(i, j)

			if i+1 < matrixLen && (*matrix)[i+1][j] == WATER {
				queue = append(queue, ItemX{i: i + 1, j: j})
			}

			if i-1 >= 0 && (*matrix)[i-1][j] == WATER {
				queue = append(queue, ItemX{i: i - 1, j: j})
			}

			if j+1 < rowLen && (*matrix)[i][j+1] == WATER {
				queue = append(queue, ItemX{i: i, j: j + 1})
			}

			if j-1 >= 0 && (*matrix)[i][j-1] == WATER {
				queue = append(queue, ItemX{i: i, j: j - 1})
			}
		}
	}

	// create a queue
	// push the first item
	// do while queue contains an item
	/* push
	i+1, j
	i-1, j
	i, j-1
	i, j+1
	*/

	fmt.Println("explore FINISH >> length: ", length, "; visitedX:", visitedX)

	return length
}

func RiverSizes(matrix Matrix) []int {
	visitedX = make(map[string]bool)

	var lengths = make([]int, 0)

	for i := range matrix {
		for j := range matrix[i] {
			if matrix[i][j] == WATER && !isVisited(i, j) {
				lengths = append(lengths, explore(&matrix, i, j))
			}
		}
	}
	return lengths
}

func main() {
	// matrix := make(Matrix, 5)
	// matrix =
	// 	Matrix{
	// 		[]int{1, 0, 0, 1, 0},
	// 		[]int{1, 0, 1, 0, 0},
	// 		[]int{0, 0, 1, 0, 1},
	// 		[]int{1, 0, 1, 0, 1},
	// 		[]int{1, 0, 1, 1, 0},
	// 	}

	matrix := make(Matrix, 1)
	matrix =
		// Matrix{
		// 	[]int{1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0},
		// 	[]int{1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0},
		// 	[]int{0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1},
		// 	[]int{1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0},
		// 	[]int{1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1},
		// }
		Matrix{
			[]int{0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0},
			[]int{0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0},
			[]int{0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1},
			[]int{0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0},
			[]int{0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0},
		}

	fmt.Println(RiverSizes(matrix))
}
