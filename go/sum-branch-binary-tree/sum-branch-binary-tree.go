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
6
3
10
37
1
10000000000000000
15

выходные данные
4
18
71
1
19999999999999980
26

1
2,3
4,5, 6,7
8,9,10,11, 12,13,14,15
16,17,18,19, 20,21,22,23, 24,25,26,27, 28,29,30,31
                                                ...., 63
                                                                                                ...., 127

1
2
4
8
16
32
64

21-15=6
6/2=3

21
int(21/2)=10
int(5/2)=2
int(2/2)=1

n/2
*/

func readInput() []int {
	var casesNumber int
	cases := make([]int, 0)

	fmt.Fscan(in, &casesNumber)

	for i := 0; i < casesNumber; i++ {
		var node int
		fmt.Fscan(in, &node)

		cases = append(cases, node)
	}

	return cases
}

func calculate(cases []int) []int {
	results := make([]int, 0)

	for i := 0; i < len(cases); i++ {
		node := cases[i]
		sum := node

		for node > 1 {
			node = int(node / 2)
			sum += node
		}

		results = append(results, sum)
	}

	return results
}

func main() {
	// fmt.Println("START >> ")
	cases := readInput()

	// fmt.Println("1 >> ", cases)

	results := calculate(cases)

	for i := 0; i < len(results); i++ {
		result := results[i]
		fmt.Println(result)
	}

	defer out.Flush()
}
