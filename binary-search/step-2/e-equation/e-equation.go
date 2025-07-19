package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var in = bufio.NewReader(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

/*
Входные данные
В единственной строке содержится вещественное число C (1.0≤c≤10^10).

Выходные данные
Выведите одно число — искомый x. Ответ будет признан верным, если относительная или абсолютная погрешность не более 10−6.



входные данные
2.0
выходные данные
1.0

входные данные
15.6
выходные данные
3.698232168829691

10e-6


eq := x*x + math.Sqrt(x)

eq = C + err || C - err

5.00001XXX
4.99999XXX

left, right

0..sqrt(C)

*/

func readInput() float64 {
	var num float64

	fmt.Fscan(in, &num)

	return num
}

// func calculate(array []int, target int) float64 {
// 	var left float64 = 0
// 	var right float64 = 1e8

// 	for i := 0; i < 100; i++ {
// 		middle := (right + left) * 0.5

// 		if good(array, middle, target) {
// 			left = middle
// 		} else {
// 			right = middle
// 		}
// 	}

// 	return left
// }

func good(x float64, c float64) bool {
	err := 1e-8
	eq := x*x + math.Sqrt(x)

	// fmt.Println("4 >> ", x, c, eq)

	return c <= eq+err
}

func calculate(c float64) float64 {
	var left float64 = 0
	var right float64 = c
	var middle float64 = 0

	// fmt.Println("3 >> ", left, right)

	for i := 0; i < 100; i++ {
		middle = (right + left) * 0.5

		if good(middle, c) {
			right = middle
		} else {
			left = middle
		}
	}

	return middle
}

func main() {
	// fmt.Println("START >> ")
	num := readInput()

	// fmt.Println("1 >> ", num)

	x := calculate(num)

	fmt.Println(x)

	defer out.Flush()
}
