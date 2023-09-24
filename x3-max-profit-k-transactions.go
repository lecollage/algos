package main

import (
	"fmt"
	"math"
)

var prices = make([]int, 0)
var knownSums = make(map[string]int)
var maxTransactionsCount = 0

func buildKeyX3(price int, index int, sign int) string {
	return fmt.Sprintf("%d|%d", index, price*sign)
}

func isKnownSum(index int, sign int) bool {
	key := buildKeyX3(prices[index], index, sign)
	_, ok := knownSums[key]

	return ok
}

func getKnownSum(index int, sign int) int {
	key := buildKeyX3(prices[index], index, sign)
	value := knownSums[key]

	return value
}

func setSum(index int, sign int, profit int) {
	key := buildKeyX3(prices[index], index, sign)

	knownSums[key] = profit
}

func calculateProfit(current int, sign int, transactionsCount int) int {
	fmt.Println()
	fmt.Println(`calculateProfit START >> current: `, current, `; sign: `, sign, `; transactionsCount: `, transactionsCount)
	//if isKnownSum(current, sign) {
	//	return getKnownSum(current, sign)
	//}

	if transactionsCount == 0 {
		//if current == len(prices)-1 {
		//	return math.MinInt
		//}

		return prices[current] * sign
	}

	next := current + 1

	if next == len(prices) {
		return prices[current] * sign
	}

	maxProfit := math.MinInt
	for ; next < len(prices); next++ {
		sum := sign * prices[next]
		nextSign := sign * -1
		profit := sum + calculateProfit(next, nextSign, transactionsCount-1)

		setSum(next, sign, profit)

		if profit > maxProfit {
			maxProfit = profit
		}
	}

	fmt.Println(`calculateProfit STEP 1 >> maxProfit: `, maxProfit)

	return maxProfit
}

func MaxProfitWithKTransactions(pricesPar []int, k int) int {
	prices = pricesPar
	maxTransactionsCount = k
	transactionsCount := k * 2

	maxProfit := math.MinInt
	for i := 0; i < len(prices)-1; i++ {
		sign := -1
		sum := sign * (prices[i])
		nextSign := sign * -1
		profit := sum + calculateProfit(i, nextSign, transactionsCount-1)

		if profit > maxProfit {
			maxProfit = profit
		}
	}

	return maxProfit
}

func main() {
	prices := []int{5, 11, 3, 50, 60, 90}
	k := 2
	fmt.Println("FINAL profit: ", MaxProfitWithKTransactions(prices, k))
	//fmt.Println("knownSums: ", knownSums)
}
