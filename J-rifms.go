package main

import (
	"bufio"
	"fmt"
	"os"
)

var inJ = bufio.NewReader(os.Stdin)
var outJ = bufio.NewWriter(os.Stdout)

var dictionaryWords = make([]string, 0)
var requestWords = make([]string, 0)

var dictionarySize = 0
var requestsSize = 0

var suffixDictionary = make(map[string][]string)

type SubSuffixResult struct {
	subDictionary map[string]string
	index         int
}

/*
3
task
decide
id
6
flask
code
void
forces
id
ask
*/

func readAllWords() {
	// words
	fmt.Fscan(inJ, &dictionarySize)

	dictionaryWords = readWords(dictionarySize)

	//requests
	fmt.Fscan(inJ, &requestsSize)
	requestWords = readWords(requestsSize)
}

func buildDictionary() {
	//fmt.Println("dictionaryWords: ", dictionaryWords)
	//fmt.Println("requestWords: ", requestWords, requestWords[0], len(requestWords))

	c := make(chan SubSuffixResult)

	for i := 0; i < dictionarySize; i++ {
		go addToSuffixDictionary(dictionaryWords[i], i, c)
	}

	for i := 0; i < dictionarySize; i++ {
		result := <-c

		for suffix, word := range result.subDictionary {
			//fmt.Printf("suffix[%s] word[%s]\n", suffix, word)

			suffixDictionary[suffix] = append(suffixDictionary[suffix], word)
		}
	}

	//fmt.Println("suffixDictionary: ", suffixDictionary)
}

func addToSuffixDictionary(word string, i int, c chan SubSuffixResult) {
	//substring := word[1:]
	subDictionary := make(map[string]string)

	//subDictionary[substring] = word

	for i := 0; i < len(word); i++ {
		substring := word[i:]

		subDictionary[substring] = word
	}

	c <- SubSuffixResult{index: i, subDictionary: subDictionary}
}

func readWords(size int) []string {
	var words = make([]string, 0)

	for j := 0; j < size; j++ {
		var word string

		fmt.Fscan(inJ, &word)

		//fmt.Println("word: ", word)

		words = append(words, word)
	}

	return words
}

func analyzeRequestWords() {
	for _, request := range requestWords {
	out:
		for i := 0; i < len(request); i++ {
			substring := request[i:]

			words, ok := suffixDictionary[substring]

			for _, word := range words {
				if ok && word != request {
					//fmt.Fprintln(outJ, "request: ", request, "; substring: ", substring, "word: ", word)
					fmt.Fprintln(outJ, word)
					break out
				}
			}

			if len(substring) < 2 {
				//fmt.Fprintln(outJ, "request: ", request, "; substring: ", substring, "no word found ", dictionaryWords[0])
				fmt.Fprintln(outJ, dictionaryWords[0])
				break out
			}
		}
	}
}

func main() {
	//fmt.Println("START >> ")
	readAllWords()

	buildDictionary()

	analyzeRequestWords()

	defer outJ.Flush()
}
