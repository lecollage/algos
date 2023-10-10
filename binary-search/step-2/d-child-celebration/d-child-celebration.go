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
	"os"
	"sort"
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

// после надувания zi шариков устает и отдыхает yi минут
func calculateLengths(workers []Worker, baloonsCount int) []int {
	lenghts := make([]int, 0)

	for _, worker := range workers {
		lenght := worker.t * baloonsCount
		var restCount int

		if baloonsCount%worker.z == 0 {
			restCount = baloonsCount / worker.z
		} else {
			restCount = int(baloonsCount / worker.z)
		}

		lenght += worker.y * restCount
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

func howManyBaloonsMayProduce(availableTime int, worker Worker) int {
	if availableTime < worker.t {
		return 0
	}

	if availableTime/worker.t <= worker.z {
		return int(availableTime / worker.t)
	}

	// 1
	// workTime := worker.t * worker.z
	// restTime := worker.y
	// sessionTime := workTime + restTime

	// availableTime -= sessionTime

	// return worker.z + howManyBaloonsMayProduce(availableTime, worker)

	// 2
	// baloons := 0

	// for availableTime > 0 {
	// 	for i := 0; i < worker.z; i++ {
	// 		availableTime -= worker.t

	// 		if availableTime < 0 {
	// 			return baloons
	// 		}

	// 		baloons++
	// 	}

	// 	availableTime -= worker.y
	// }

	// 3

	if availableTime%(worker.t*worker.z+worker.y) == 0 {
		return availableTime / (worker.t*worker.z + worker.y)
	}

	sessions := availableTime / (worker.t*worker.z + worker.y)
	baloons := sessions * worker.z

	availableTime -= sessions * (worker.t*worker.z + worker.y)

	for availableTime > 0 {
		for i := 0; i < worker.z; i++ {
			availableTime -= worker.t

			if availableTime < 0 {
				return baloons
			}

			baloons++
		}

		availableTime -= worker.y
	}

	return baloons
}

func canProduceBaloons(availableTime int, workers []Worker, baloonsCount int) (bool, []Worker) {
	commonBaloonsCount := 0
	busyWorkers := make([]Worker, 0)

	for _, worker := range workers {
		// fmt.Println("7 >> worker: ", worker, availableTime, howManyBaloonsMayProduce(availableTime, worker))
		workerBaloons := howManyBaloonsMayProduce(availableTime, worker)
		busyWorkers = append(busyWorkers, Worker{t: worker.t, z: worker.z, y: worker.y, work: workerBaloons, id: worker.id})
		commonBaloonsCount += workerBaloons

		// fmt.Println("8 >> commonBaloonsCount: ", commonBaloonsCount)
		if commonBaloonsCount >= baloonsCount {
			return true, busyWorkers
		}
	}

	// fmt.Println("9 >> commonBaloonsCount: ", commonBaloonsCount)

	return false, busyWorkers
}

func calculate(workers []Worker, baloonsCount int) (int, []Worker) {
	lengths := calculateLengths(workers, baloonsCount)
	maxLength := getMaxLength(lengths)

	// fmt.Println("5 >> lengths: ", lengths, "; maxLength: ", maxLength)

	var left int = baloonsCount
	var right int = maxLength

	for left != right {
		var middle = int((left + right) / 2)
		var can bool

		// fmt.Println("6 >> lengths: ", left, middle, right)
		can, workers = canProduceBaloons(middle, workers, baloonsCount)
		if can {
			right = middle
		} else {
			left = middle
		}
	}

	return left, workers
}

func findWorkerById(workers []Worker, id int) *Worker {
	for i := 0; i < len(workers); i++ {
		if workers[i].id == id {
			return &workers[i]
		}
	}

	return nil
}

func main() {
	// fmt.Println("START >> ")
	workers, baloonsCount := readInput()

	sort.Slice(workers, func(i, j int) bool {
		return workers[i].t < workers[j].t
	})

	// fmt.Println("1 >> ", workers, baloonsCount)

	minLength, busyWorkers := calculate(workers, baloonsCount)

	sort.Slice(workers, func(i, j int) bool {
		return workers[i].id < workers[j].id
	})

	fmt.Println(minLength)
	// fmt.Println("busyWorkers: ", busyWorkers)
	for i := 0; i < len(workers); i++ {
		busyWorker := findWorkerById(busyWorkers, workers[i].id)

		if busyWorker != nil {
			fmt.Print(busyWorker.work, " ")
		} else {
			fmt.Print("0 ")
		}
	}

	defer out.Flush()
}

/*
-OXXX
OOXXO0
*/
