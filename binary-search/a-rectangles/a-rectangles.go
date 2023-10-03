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
2 3 10

выходные данные
9

0, 100
0, 50
0, 25
0, 12
6, 12 -> 9
6, 9 -> 7
*/

func readInput() (int, int, int) {
	var width, height, number int

	fmt.Fscan(in, &width)
	fmt.Fscan(in, &height)
	fmt.Fscan(in, &number)

	return width, height, number
}

func good(width, height, number, middle int) bool {
	return int((middle/width))*int((middle/height)) >= number
}

func calculate(width, height, number int) int {
	left := 0
	right := 1
	middle := 0

	for !good(width, height, number, right) {
		right *= 2
	}

	for right > left+1 {
		middle = int((left + right) / 2)

		if good(width, height, number, middle) {
			right = middle
		} else {
			left = middle
		}
	}

	return right
}

func main() {
	// fmt.Println("START >> ")
	width, height, number := readInput()

	// fmt.Println("1 >> ", width, height, number)

	result := calculate(width, height, number)

	fmt.Println(result)

	defer out.Flush()
}
