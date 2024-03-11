package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

//
//import (
//	"bufio"
//	"fmt"
//	"log"
//	"os"
//	"strings"
//)
//
//func scanText(reader *bufio.Reader) []string {
//	var lines []string
//	for {
//		line, err := reader.ReadString('\n')
//		if err != nil {
//			log.Fatal(err)
//		}
//		if len(strings.TrimSpace(line)) == 0 {
//			break
//		}
//		lines = append(lines, line)
//	}
//
//	return lines
//}
//
//func main() {
//	reader := bufio.NewReader(os.Stdin)
//	text := scanText(reader)
//
//	fmt.Println("text: ", text)
//}

func main() {
	reader := bufio.NewReader(os.Stdin)

	setsCount, _ := strconv.Atoi(lines[0])

	fmt.Println("text: ", text)
}
