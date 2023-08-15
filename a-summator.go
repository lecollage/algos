package main

import (
	"bufio"
	"fmt"
	"os"
)

func summator() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var rowCount int

	fmt.Fscan(in, &rowCount)

	for i := 0; i < rowCount; i++ {
		var n1 int
		var n2 int
		fmt.Fscan(in, &n1, &n2)

		var result = n1 + n2

		fmt.Fprintln(out, result)
	}
}

func main() {
	summator()
}
