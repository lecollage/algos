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
4 11
802
743
457
539

выходные данные
200.5

*/

func readInput() ([]int, int) {
	var arraySize, number int
	array := make([]int, 0)

	fmt.Fscan(in, &arraySize)
	fmt.Fscanln(in, &number)

	for i := 0; i < arraySize; i++ {
		var elem int
		fmt.Fscan(in, &elem)

		array = append(array, elem)
	}

	return array, number
}

func good(array []int, length float32, target int) bool {
	number := 0

	for _, item := range array {
		number += int(float32(item) / length)
	}

	// fmt.Println("3 >> ", number, length)

	return number >= target
}

func calculate(array []int, target int) float32 {
	var left float32 = 0
	var right float32 = 1e8

	for i := 0; i < 100; i++ {
		middle := (right + left) * 0.5

		if good(array, middle, target) {
			left = middle
		} else {
			right = middle
		}
	}

	return left
}

func main() {
	// fmt.Println("START >> ")
	array, number := readInput()

	// fmt.Println("1 >> ", array, number)

	maxLength := calculate(array, number)

	fmt.Println(maxLength)

	defer out.Flush()
}
