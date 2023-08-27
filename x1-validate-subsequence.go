package main

import "fmt"

func _IsValidSubsequence(array []int, sequence []int) bool {

	cursor := 0

	for i, item := range sequence {
		for array[cursor] != item {
			cursor++

			if cursor == len(array) {
				return false
			}
		}

		if cursor == len(array)-1 && i != len(sequence)-1 {
			return false
		}

		if array[cursor] == item {
			cursor++
		}
	}

	return true
}

func IsValidSubsequence(array []int, sequence []int) {
	fmt.Println(_IsValidSubsequence(array, sequence))
}

func main() {
	arr := []int{5, 1, 22, 25, 6, 6, -1, 8}
	seq := []int{1, 6, 6, -1}

	IsValidSubsequence(arr, seq)
}
