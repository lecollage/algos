/*
m воздушных шариков.
n помощников
i-й среди которых надувает шарик за ti минут

после надувания zi шариков устает и отдыхает yi минут

через какое время будут надуты все шарики при наиболее оптимальной работе помощников

Входные данные
В первой строке входных данных задаются числа m и n (0≤m≤15000,1≤n≤1000).
Следующие n строк содержат по три целых числа — ti, zi и yi соответственно (1≤ti,yi≤100,1≤zi≤1000).

1 2
2 1 1
1 1 2

1
0 1


5 2
2 1 1
1 1 2

11R11R
1RR1RR

ti*m - (yi*(m/zi-1))
ti*m - (yi*(m/zi-1)) > m

m

n * X



..|..
.||.||.

..|..|
.||.||.||




m/(ti)

ai = m/ti



1. a1 + a2 + ... an >= n - move right
(a1 + a2 + ... an)/n >= a1
a1*n <= a1 + a2 + ... an
a1*(n-1) <= a2 + ... an




a1 + a2 + ... an < n - move left

..|
.||

5/3

5/2 -> 2,3

l1,l2

k1=m/l1
k2=m/l2


l1=3
l2=1
l3=2
k1=3/5 = 0.6
k2=1/5 = 0.2
k3=2/5 = 0.4

0.2, 0.4, 0.6

l1=3
l2=1
l3=2

1,2,3

3*1
2*1
1*3

-
--
---

     L
- - -|
-- --|
---  |

ai = L/ti

L = max(t1*n, t2*n, ... ti*n) = 3*5 = 15
                    L
- - - - -           | a1 = L/t1 = 15/1 = 15
-- -- -- -- --      | a2 = L/t2 = 15/2 = 7
--- --- --- --- --- | a3 = L/t3 = 15/3 = 5

15+7+5>5
L = (0 + 15)/2=7


                    L
- - - - -           | a1 = L/t1 = 7/1 = 7
-- -- -- -- --      | a2 = L/t2 = 7/2 = 3
--- --- --- --- --- | a3 = L/t3 = 7/3 = 2
7+3+2>5
L = (0 + 7)/2=3

        L
- - -   | a1 = L/t1 = 3/1 = 3
--      | a2 = L/t2 = 3/2 = 1
---     | a3 = L/t3 = 3/3 = 1
3+1+1>=5
L = (0 + 5)/2=2

     L
- -  | a1 = L/t1 = 2/1 = 2
--   | a2 = L/t2 = 2/2 = 1
     | a3 = L/t3 = 2/3 = 0
2+1<5

L = (2 + 5)/2=3

a1 + .. + an >= n

5/1
5/2
5/3



5

[ti, zi, yi]
ti zi yi


---XX---XX---|




min(min(a, b), (a + b) / 4)
min(min(a1, a2, a3, .. , an), (a1 + a2 + a3 + an) / n)
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

type Worker struct {
	t, z, y, work, id int
}

/*
1 2
2 1 1
1 1 2

В первой строке входных данных задаются числа m и n (0≤m≤15000,1≤n≤1000).
Следующие n строк содержат по три целых числа — ti, zi и yi соответственно (1≤ti,yi≤100,1≤zi≤1000).
*/
func readInput() ([]Worker, int) {
	var m, n int

	fmt.Fscan(in, &m)
	fmt.Fscan(in, &n)

	array := make([]Worker, 0)

	for i := 0; i < n; i++ {
		var t, z, y int
		fmt.Fscan(in, &t)
		fmt.Fscan(in, &z)
		fmt.Fscan(in, &y)
		worker := Worker{t: t, z: z, y: y, work: 0, id: i}

		// fmt.Println(worker)

		array = append(array, worker)
	}

	return array, m
}

/*
si = zi * ti + yi
Tfull=T/si

1 2
2 1 1
1 1 2
-> 1



3 2
2 2 5
1 1 10
-> 4
*/

func canProduceBaloons(time int, workers []Worker, baloonsCount int) bool {
	commonBaloonsCount := 0

	for _, worker := range workers {
		cycleTime := worker.z*worker.t + worker.y
		fullCyclesCount := int(time / cycleTime)

		commonBaloonsCount += fullCyclesCount * worker.z

		restTime := time % cycleTime
		restBaloonsCount := int(restTime / worker.t)

		if restBaloonsCount <= worker.z {
			commonBaloonsCount += restBaloonsCount
		} else {
			commonBaloonsCount += worker.z
		}

		if commonBaloonsCount >= baloonsCount {
			return true
		}
	}

	return false
}

func calculate(workers []Worker, baloonsCount int) int {
	var left int = -1
	var right int = math.MaxInt

	for left+1 < right {
		var middle = int((left + right) / 2)

		if canProduceBaloons(middle, workers, baloonsCount) {
			right = middle
		} else {
			left = middle
		}
	}

	return right
}

func main() {
	// fmt.Println("START >> ")
	workers, baloonsCount := readInput()
	time := calculate(workers, baloonsCount)

	fmt.Println(time)

	requiredBaloonsCount := baloonsCount

	for _, worker := range workers {
		cycleTime := worker.z*worker.t + worker.y
		fullCyclesCount := int(time / cycleTime)
		currBaloonsCount := fullCyclesCount * worker.z
		restTime := time % cycleTime
		restBaloonsCount := int(restTime / worker.t)

		if restBaloonsCount <= worker.z {
			currBaloonsCount += restBaloonsCount
		} else {
			currBaloonsCount += worker.z
		}

		if requiredBaloonsCount <= 0 {
			fmt.Print(0, " ")
		} else if requiredBaloonsCount < currBaloonsCount {
			fmt.Print(requiredBaloonsCount, " ")
		} else {
			fmt.Print(currBaloonsCount, " ")
		}

		requiredBaloonsCount -= currBaloonsCount
	}

	defer out.Flush()
}

/*
-OXXX
OOXXO0
*/
