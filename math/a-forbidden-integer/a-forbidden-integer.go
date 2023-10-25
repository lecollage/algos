package main

import (
	"bufio"
	"fmt"
	"os"
)

var in = bufio.NewReader(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

/*
5
10 3 2
5 2 1
4 2 1
7 7 3
6 1 1

x ≤ k ≤ n
*/

func readCase() (int, int, int) {
	var n, k, x int
	fmt.Fscan(in, &n)
	fmt.Fscan(in, &k)
	fmt.Fscan(in, &x)

	return n, k, x
}

// 10 3 2 -> 10%3 = 1 , 1 % 1
func calculate(n int, k int, x int) (bool, []int) {
	var arr = make([]int, 0)
	for n > 0 && k > 0 {
		if k <= n && k != x {
			div := int(n / k)

			fmt.Println("div: ", div)

			n -= (div * k)

			for i := 0; i < div; i++ {
				arr = append(arr, k)
			}
		}

		k--
	}

	fmt.Println(n, k)

	if n == 0 {
		return true, arr
	}

	return false, []int{}
}

func main() {
	var casesNum int
	fmt.Fscan(in, &casesNum)

	for casesNum > 0 {
		n, k, x := readCase()
		result, array := calculate(n, k, x)

		if result {
			fmt.Println("YES")
			fmt.Println(len(array))
			for i, item := range array {
				if i == len(array)-1 {
					fmt.Println(item)
				} else {
					fmt.Print(item, " ")
				}
			}
		} else {
			fmt.Println("NO")
		}

		casesNum--
	}
}
