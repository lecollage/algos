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
4 1 1
выходные данные
3

4 - min(1, 1) = 3
3

3 / (1+1) = 1


входные данные
5 1 2
выходные данные
4

5 - min(1,2) = 4

4 - 1*2+2*2

4
.. ..
. .

4
2
4

4-2*1
2-1*2


100

2
3

100/2 * 2, 100/3 * 2,

.. .. .. .. ..
... ... ... ...


2*x + 3*y == N

.

. . . .


.. ..

x*3 + y*1 == 4

4/1 = 4
4/2=2

min(n * min(x, y), ceil(n/2) * x + floor(n/2) * y)
min(4 * min(1, 2), ceil(4/2) * 1 + floor(4/2) * 2)

3
1

3*1 - 1*2


1*4
2*0

1*3
2*1

1*2
2*2


c1*x
c2*y

M=N-1
x+y=M
1,2,3,4
l m r

1, 10
99


c1*x+c2*y




minDiff

|c1*x-c2*y| -> min

M-x=y

0..M

l,m,r

l:0
r:M




5 1 2
выходные данные
4



10 1 2
выходные данные
4

9
.
. . . . . .
.. .. ..

*/

func readInput() (int, int, int) {
	var pageCount, cost1, cost2 int

	fmt.Fscan(in, &pageCount)
	fmt.Fscan(in, &cost1)
	fmt.Fscan(in, &cost2)

	return pageCount, cost1, cost2
}

func min(x int, y int) int {
	if x < y {
		return x
	}

	return y
}

func canCopy(curr, pageCount, cost1, cost2 int) bool {
	cnt := 0
	minCost := min(cost1, cost2)

	if curr < minCost {
		cnt = 0
	} else {
		cnt = 1 + (curr-minCost)/cost1 + (curr-minCost)/cost2
	}

	return cnt >= pageCount
}

func calculate(pageCount int, cost1 int, cost2 int) int {
	minCost := cost1

	if cost2 < cost1 {
		minCost = cost2
	}

	var left int = 0
	var right int = minCost * pageCount

	for left+1 < right {
		m := int((left + right) / 2)

		if canCopy(m, pageCount, cost1, cost2) {
			right = m
		} else {
			left = m
		}
	}

	// fmt.Println("5 >> left: ", left)

	return right
}

func main() {
	// fmt.Println("START >> ")
	pageCount, cost1, cost2 := readInput()

	// fmt.Println("1 >> ", pageCount, cost1, cost2)

	maxLength := calculate(pageCount, cost1, cost2)

	fmt.Println(maxLength)

	defer out.Flush()
}
