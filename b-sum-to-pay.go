package main

import (
	"bufio"
	"fmt"
	"os"
)

func calculateSumToPay() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var setsCount int

	fmt.Fscan(in, &setsCount)

	for i := 0; i < setsCount; i++ {
		var goodsCount int
		fmt.Fscan(in, &goodsCount)

		pricesMap := make(map[int]int)
		var prices = make([]int, goodsCount)

		// fill the map
		for j := 0; j < goodsCount; j++ {
			var price int

			fmt.Fscan(in, &price)

			prices[j] = price

			_, present := pricesMap[price]

			if !present {
				pricesMap[price] = 1
			} else {
				pricesMap[price]++
			}
		}

		var sum = 0

		// process the map
		for price, count := range pricesMap {
			sum += (count - int(count/3)) * price
			//fmt.Fprintln(out, price, count, count%3, sum)
		}

		//fmt.Fprintln(out, goodsCount, prices, pricesMap, sum)
		fmt.Fprintln(out, sum)
	}
}

func main() {
	calculateSumToPay()
}
