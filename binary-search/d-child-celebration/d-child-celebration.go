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
	"os"
	"sort"
)

var in = bufio.NewReader(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

type Helper struct {
	t, z, y, work int
}

/*
1 2
2 1 1
1 1 2

В первой строке входных данных задаются числа m и n (0≤m≤15000,1≤n≤1000).
Следующие n строк содержат по три целых числа — ti, zi и yi соответственно (1≤ti,yi≤100,1≤zi≤1000).
*/
func readInput() ([]Helper, int) {
	var m, n int

	fmt.Fscan(in, &m)
	fmt.Fscan(in, &n)

	array := make([]Helper, 0)

	for i := 0; i < n; i++ {
		var t, z, y int
		fmt.Fscan(in, &t)
		fmt.Fscan(in, &z)
		fmt.Fscan(in, &y)

		array = append(array, Helper{t: t, z: z, y: y, work: 0})
	}

	return array, m
}

// после надувания zi шариков устает и отдыхает yi минут
func calculateLengths(helpers []Helper, baloonsCount int) []int {
	lenghts := make([]int, 0)

	for _, helper := range helpers {
		lenght := helper.t * baloonsCount
		var restCount int

		if baloonsCount%helper.z == 0 {
			restCount = baloonsCount / helper.z
		} else {
			restCount = int(baloonsCount / helper.z)
		}

		lenght += helper.y * restCount
		lenghts = append(lenghts, lenght)
	}

	return lenghts
}

func getMaxLength(lengths []int) int {
	max := lengths[0]

	for _, l := range lengths {
		if l > max {
			max = l
		}
	}

	return max
}

/*
-OXXX
OOXXO0


-OXXX|
OOXXO|
| -> 0
0| -> 1 availTime / t

OOX|

OOXX|O
*/

func howManyBaloonsMayProduce(availableTime int, helper Helper) int {
	if availableTime < helper.t {
		return 0
	}

	if availableTime/helper.t <= helper.z {
		return int(availableTime / helper.t)
	}

	workTime := helper.t * helper.z
	restTime := helper.y
	sessionTime := workTime + restTime

	availableTime -= sessionTime

	return helper.t*helper.z + howManyBaloonsMayProduce(availableTime, helper)
}

func canProduceBaloons(availableTime int, helpers []Helper, baloonsCount int) (bool, []Helper) {
	commonBaloonsCount := 0

	workHelpers := make([]Helper, 0)

	for _, helper := range helpers {
		// fmt.Println("7 >> helper: ", helper, availableTime, howManyBaloonsMayProduce(availableTime, helper))
		helperBaloons := howManyBaloonsMayProduce(availableTime, helper)
		workHelpers = append(workHelpers, Helper{t: helper.t, z: helper.z, y: helper.y, work: helperBaloons})
		commonBaloonsCount += helperBaloons

		// fmt.Println("8 >> commonBaloonsCount: ", commonBaloonsCount)
		if commonBaloonsCount >= baloonsCount {
			return true, workHelpers
		}
	}

	// fmt.Println("9 >> commonBaloonsCount: ", commonBaloonsCount)

	return false, workHelpers
}

func calculate(helpers []Helper, baloonsCount int) (int, []Helper) {
	lengths := calculateLengths(helpers, baloonsCount)
	maxLength := getMaxLength(lengths)

	// fmt.Println("5 >> lengths: ", lengths, "; maxLength: ", maxLength)

	var left int = baloonsCount
	var right int = maxLength
	var middle = int((left + right) / 2)
	// var work = make([]int, 0)

	for left != right {
		middle = int((left + right) / 2)

		var can bool

		// fmt.Println("6 >> lengths: ", left, middle, right)
		can, helpers = canProduceBaloons(middle, helpers, baloonsCount)
		if can {
			right = middle
		} else {
			left = middle
		}
	}

	return left, helpers
}

func main() {
	// fmt.Println("START >> ")
	helpers, baloonsCount := readInput()

	// fmt.Println("1 >> ", helpers, baloonsCount)

	sort.Slice(helpers, func(i, j int) bool {
		return helpers[i].t < helpers[j].t
	})

	minLength, helpers := calculate(helpers, baloonsCount)

	fmt.Println(minLength)
	fmt.Println("helpers: ", helpers)
	// for i := 0; i < len(helpers); i++ {
	// 	if i < len(work) {
	// 		fmt.Print(work[i], " ")
	// 	} else {
	// 		fmt.Print("0 ")
	// 	}
	// }

	defer out.Flush()
}

/*
-OXXX
OOXXO0
*/
