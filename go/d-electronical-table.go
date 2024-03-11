package main

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func processTable() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var setsCount int

	fmt.Fscan(in, &setsCount)

	for i := 0; i < setsCount; i++ {
		// read set
		/*
			4 3
			3 4 1
			2 2 5
			2 4 2
			2 2 1
			3
			2 1 3
		*/

		// read matrix description
		var rowsCount, columnsCount int
		fmt.Fscan(in, &rowsCount, &columnsCount)

		// read matrix
		var matrix = make([][]int, rowsCount)

		for i := 0; i < rowsCount; i++ {
			matrix[i] = make([]int, columnsCount)
			for j := 0; j < columnsCount; j++ {
				var number int
				fmt.Fscan(in, &number)

				matrix[i][j] = number
			}
		}

		//fmt.Fprintln(out, matrix)

		// read number of actions
		var actionsCount int
		fmt.Fscan(in, &actionsCount)

		// read actions
		var actions = make([]int, actionsCount)

		for i := 0; i < actionsCount; i++ {
			var action int

			fmt.Fscan(in, &action)
			actions[i] = action
		}

		// sort matrix according to actions
		for _, action := range actions {
			sort.SliceStable(matrix, func(i, j int) bool {
				var columnIndexToSort = action - 1

				return matrix[i][columnIndexToSort] < matrix[j][columnIndexToSort]
			})
		}

		//fmt.Fprintln(out, actionsCount, actions)
		//fmt.Fprintln(out, matrix)

		for _, row := range matrix {
			var buffer bytes.Buffer
			for _, value := range row {
				buffer.WriteString(" ")
				buffer.WriteString(strconv.Itoa(value))
			}
			fmt.Fprintln(out, buffer.String())
		}

		fmt.Fprintln(out)
	}
}

func main() {
	processTable()
}
