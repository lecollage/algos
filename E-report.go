package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

var inE = bufio.NewReader(os.Stdin)
var outE = bufio.NewWriter(os.Stdout)

type AnalyzeResultE struct {
	result bool
	index  int
}

func containsE[T comparable](s []T, e T) bool {
	for _, v := range s {
		if v == e {
			return true
		}
	}
	return false
}

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

	c := make(chan AnalyzeResultE)

	results := make([]AnalyzeResultE, setsCount)

	for i := 0; i < setsCount; i++ {
		var setLength int

		fmt.Fscan(inE, &setLength)

		var items []int

		for j := 0; j < setLength; j++ {
			var item int

			fmt.Fscan(inE, &item)

			items = append(items, item)
		}

		go analyzeItems(items, i, c)
	}

	//fmt.Println(results)

	for i := 0; i < setsCount; i++ {
		result := <-c

		results[i] = result
	}

	printResultsE(results)
}

func printResultsE(results []AnalyzeResultE) {
	sort.Slice(results, func(i, j int) bool {
		return results[i].index < results[j].index
	})

	for _, result := range results {
		if result.result {
			//fmt.Fprintln(outE, "YES", result.index)
			fmt.Fprintln(outE, "YES")
		} else {
			//fmt.Fprintln(outE, "NO", result.index)
			fmt.Fprintln(outE, "NO")
		}
	}
}

func analyzeItems(items []int, index int, c chan AnalyzeResultE) {
	currentItem := items[0]
	processedItems := make(map[int]bool)
	processedItems[items[0]] = true

	for _, item := range items {
		if item != currentItem {
			if !processedItems[item] {
				processedItems[item] = true
				currentItem = item
			} else {
				c <- AnalyzeResultE{index: index, result: false}
				return
			}
		}
	}

	c <- AnalyzeResultE{index: index, result: true}
}

func main() {
	//fmt.Println("START >> ")
	readReportsAndAnalyze()

	defer outE.Flush()
}
