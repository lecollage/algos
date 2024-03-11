package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

var inC = bufio.NewReader(os.Stdin)
var outC = bufio.NewWriter(os.Stdout)

type AnalyzeResultC struct {
	result [][]int
	index  int
}

/*
3

6
2 1 3 1 1 4

2
5 5

8
1 4 2 5 4 2 6 3
*/
func readAndAnalyzeE() {
	var setsCount int

	fmt.Fscan(inC, &setsCount)

	c := make(chan AnalyzeResultC)

	results := make([]AnalyzeResultC, setsCount)

	for i := 0; i < setsCount; i++ {
		items := readItems()

		go analyzeProgrammers(items, i, c)
	}

	//fmt.Println(results)

	for i := 0; i < setsCount; i++ {
		result := <-c

		results[i] = result
	}

	printResultsC(results)
}

func readItems() []int {
	var setLength int

	fmt.Fscan(inC, &setLength)

	var items []int

	for j := 0; j < setLength; j++ {
		var item int

		fmt.Fscan(inC, &item)

		items = append(items, item)
	}

	return items
}

func printResultsC(results []AnalyzeResultC) {
	sort.Slice(results, func(i, j int) bool {
		return results[i].index < results[j].index
	})

	for i, result := range results {
		for _, pair := range result.result {
			for _, item := range pair {
				fmt.Fprint(outC, item, " ")
			}
			fmt.Fprintln(outC)
		}

		if i != len(results)-1 {
			fmt.Fprintln(outC)
		}
	}
}

/*
1 4 2 5 4 2 6 3
*/

func analyzeProgrammers(skills []int, index int, c chan AnalyzeResultC) {
	processed := make(map[int]bool)
	pairs := make([][]int, 0)

	currentIndex := 0

	//fmt.Println("analyzeProgrammers START >> ", skills, processed)

	for len(processed) != len(skills) {
		pair := make([]int, 0)
		current := skills[currentIndex]

		minDiff := math.MaxInt
		minDiffIndex := -1
		i := currentIndex + 1

		//fmt.Println("analyzeProgrammers STEP 1 >> current: ", current, "; processed: ", processed)
		if !processed[currentIndex] {
			for ; i < len(skills); i++ {
				diff := current - skills[i]

				if diff < 0 {
					diff = -diff
				}

				if diff < minDiff && !processed[i] {
					minDiff = diff
					minDiffIndex = i

					//fmt.Println("analyzeProgrammers STEP 10 >> minDiff: ", minDiff)
				}
			}

			pair = append(pair, currentIndex+1)
			pair = append(pair, minDiffIndex+1)
			pairs = append(pairs, pair)
			processed[currentIndex] = true
			processed[minDiffIndex] = true
		}

		currentIndex++
	}

	c <- AnalyzeResultC{index: index, result: pairs}
}

func main() {
	//fmt.Println("START >> ")
	readAndAnalyzeE()

	defer outC.Flush()
}
