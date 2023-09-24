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

5 5

10 1
2 3
0 0
17 2
1000000000 1000000000

выходные данные
2
1
1
0
2
500000000


10 15

(10+15)/4=6 max

6

10-15 > 3 ?

1,3-9,12
1,3-8,9
2,2-6,7
2,2-4,5
2,2-2,3
2,2-0,1

17,2
17-2=15 > 3
3,1
3,1

1,3
2,2
3,1

2,2
2,2
2,2
2,2
2,2

29,11
3,1-26,10
3,1-23,9
3,1-20,8
3,1-17,7
3,1-14,6
3,1-11,5
3,1-8,4
3,1-5,3
2,2-3,1
3,1-0,0

		for current.maths > 0 && current.progers > 0 && current.maths+current.progers >= 4 {
			if current.maths-current.progers >= 3 {
				current.maths -= 3
				current.progers -= 1
			} else if current.progers-current.maths >= 3 {
				current.maths -= 1
				current.progers -= 3
			} else {
				current.maths -= 2
				current.progers -= 2
			}
			teams++
		}

		for current.maths > 0 && current.progers > 0 && current.maths+current.progers >= 4 {
			if current.maths-current.progers >= 3 {
				current.maths -= 3
				current.progers -= 1
				teams++
			} else if current.progers-current.maths >= 3 {
				current.maths -= 1
				current.progers -= 3
				teams++
			} else if current.progers+current.maths == 4 && current.progers != current.maths {
				if current.maths > current.progers {
					current.maths -= 3
					current.progers -= 1
				} else {
					current.maths -= 1
					current.progers -= 3
				}
				teams++
			} else {
				min := current.maths

				if current.progers < current.maths {
					min = current.progers
				}

				pairs := int(min / 2)
				teams += pairs
				current.progers -= (pairs * 2)
				current.maths -= (pairs * 2)

				// fmt.Println("2 >> ", current)
			}
		}

*/

type Case struct {
	maths   int
	progers int
}

func readInput() []Case {
	var casesNumber int
	cases := make([]Case, 0)

	fmt.Fscan(in, &casesNumber)

	for i := 0; i < casesNumber; i++ {
		var maths, progers int
		fmt.Fscan(in, &maths)
		fmt.Fscan(in, &progers)

		cases = append(cases, Case{maths: maths, progers: progers})
	}

	return cases
}

func calculate(cases []Case) []int {
	results := make([]int, 0)

	for i := 0; i < len(cases); i++ {
		current := cases[i]

		teams := 0

		for current.maths > 0 && current.progers > 0 && current.maths+current.progers >= 4 {
			if current.maths-current.progers >= 3 {
				diff := current.maths - current.progers
				pairs := int(diff / 3)

				if pairs > current.progers {
					pairs = current.progers
				}

				teams += pairs
				current.progers -= pairs
				current.maths -= (pairs * 3)
			} else if current.progers-current.maths >= 3 {
				diff := current.progers - current.maths
				pairs := int(diff / 3)

				if pairs > current.maths {
					pairs = current.progers
				}

				teams += pairs
				current.progers -= (pairs * 3)
				current.maths -= pairs
			} else if current.progers+current.maths == 4 && current.progers != current.maths {
				if current.maths > current.progers {
					current.maths -= 3
					current.progers -= 1
				} else {
					current.maths -= 1
					current.progers -= 3
				}
				teams++
			} else {
				min := current.maths

				if current.progers < current.maths {
					min = current.progers
				}

				pairs := int(min / 2)
				teams += pairs
				current.progers -= (pairs * 2)
				current.maths -= (pairs * 2)

				// fmt.Println("2 >> ", current)
			}
		}

		results = append(results, teams)
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
