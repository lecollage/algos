package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var inE = bufio.NewReader(os.Stdin)
var outE = bufio.NewWriter(os.Stdout)

/*
5

5
1 2 3 4 5

4
1 2 3 1
8
2 3 4 8 5 5 5 5
5
1 1 3 2 2
5
1 1 2 3 2
*/
func numbers(s string) []int {
	var n []int
	for _, f := range strings.Fields(s) {
		i, err := strconv.Atoi(f)
		if err == nil {
			n = append(n, i)
		}
	}
	return n
}

func getInputSlice() []int {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	return numbers(scanner.Text())

}

func readReportsAndAnalyze() {
	var setsCount int

	fmt.Fscan(inE, &setsCount)

	for i := 0; i < setsCount; i++ {
		var setLength int

		fmt.Fscan(inE, &setLength)

		var items []int
		items = getInputSlice()

		fmt.Println(items)
	}
}

func main() {
	fmt.Println("START >> ")
	readReportsAndAnalyze()

	defer outE.Flush()
}
