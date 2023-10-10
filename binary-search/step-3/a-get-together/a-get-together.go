/*
A. Get together
There are n people on a straight line, they need to gather at one point. Each person knows his current position xi and his speed vi.
Help them find out in what minimum time they can gather at one point.


Input
The first line contains integer n (1≤n≤105), next n lines contain pairs of integers xi and vi (−10^9≤xi≤10^9, 1≤vi≤10^9).

Output
Print one number, the minimum time it takes people to gather at one point. The answer will be considered correct if the relative or absolute error does not exceed 10^−6.
*/
/*

|xi-x|/vi

max(|xi-x|/vi) <= T
|xi-x|/vi <= T, i=1..n
|xi-x| <= T*vi

xi+T*vi, xi-T*vi = x

[xi−t⋅vi, xi+t⋅vi]
*/

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
входные данные
5
-1 5
10 3
4 2
7 10
8 1

выходные данные
1.5
*/

type Person struct {
	x int
	v int
}

func readInput() []Person {
	var arrayLength int

	fmt.Fscan(in, &arrayLength)

	array := make([]Person, 0)

	for i := 0; i < arrayLength; i++ {
		var x, v int
		fmt.Fscan(in, &x)
		fmt.Fscan(in, &v)
		array = append(array, Person{x: x, v: v})
	}

	return array
}

func good(t float64, people []Person) bool {
	maxL := float64(math.MinInt)
	minK := float64(math.MaxInt)

	for _, person := range people {
		// [xi−t⋅vi, xi+t⋅vi]
		l := float64(person.x) - t*float64(person.v)
		k := float64(person.x) + t*float64(person.v)

		if l > maxL {
			maxL = l
		}

		if k < minK {
			minK = k
		}
	}

	// fmt.Println("4 >> ", x, c, eq)

	return maxL < minK
}

func calculate(people []Person) float64 {
	var left float64 = 0
	var right float64 = 500
	var middle float64 = 0

	// fmt.Println("3 >> ", left, right)

	for i := 0; i < 100; i++ {
		middle = (right + left) * 0.5

		if good(middle, people) {
			right = middle
		} else {
			left = middle
		}
	}

	return middle
}

func main() {
	people := readInput()

	// fmt.Println("1 >> ", people)

	result := calculate(people)

	fmt.Println(result)

	defer out.Flush()
}
