package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"sort"
	"strings"
	"time"
)

var outf = bufio.NewWriter(os.Stdout)

type TimeInterval struct {
	from time.Time
	to   time.Time
}
type AnalyzeResult struct {
	result bool
	number int
}

func readSet(in *bufio.Reader) []string {
	// read set
	/*
		6
		17:53:39-20:20:02
		10:39:17-11:00:52
		08:42:47-09:02:14
		09:44:26-10:21:41
		00:46:17-02:07:19
		22:42:50-23:17:46
	*/

	// read set description
	var intervalsCount int
	fmt.Fscan(in, &intervalsCount)

	// read intervals
	var intervals = make([]string, intervalsCount)

	for i := 0; i < intervalsCount; i++ {
		var rawRow string
		fmt.Fscan(in, &rawRow)
		intervals[i] = rawRow
	}

	return intervals
}

func readAndValidateTimeIntervals(in *bufio.Reader) {
	c := make(chan AnalyzeResult)

	var setsCount int

	fmt.Fscan(in, &setsCount)

	for i := 0; i < setsCount; i++ {
		var timeIntervals = readSet(in)

		go areTimeIntervalsCorrect(timeIntervals, i, c)
	}

	results := make([]AnalyzeResult, setsCount)

	for i := 0; i < setsCount; i++ {
		result := <-c

		results[i] = result
	}

	printResults(results)
}

func printResults(results []AnalyzeResult) {
	sort.Slice(results, func(i, j int) bool {
		return results[i].number < results[j].number
	})

	for _, result := range results {
		if result.result {
			//fmt.Fprintln(outf, "YES", i)
			fmt.Fprintln(outf, "YES")
		} else {
			//fmt.Fprintln(outf, "NO", i)
			fmt.Fprintln(outf, "NO")
		}
	}
}

func areTimeIntervalsCorrect(timeIntervals []string, number int, channel chan AnalyzeResult) {
	intervals, err := validateSyntaxAndPrepare(timeIntervals)

	if err != nil {
		channel <- AnalyzeResult{result: false, number: number}
	} else {
		channel <- AnalyzeResult{result: validateIntervals(intervals), number: number}
	}
}

func validateSyntaxAndPrepare(rawIntervals []string) ([]TimeInterval, error) {
	timeIntervals := make([]TimeInterval, 0)

	for _, raw := range rawIntervals {
		raws := strings.Split(raw, "-")
		rawFrom := raws[0]
		rawTo := raws[1]

		preparedRawFrom := prepareStringDate(rawFrom)
		preparedRawTo := prepareStringDate(rawTo)

		//fmt.Fprintln(outf, "validateSyntaxAndPrepare STEP 1 >> rawFrom: ", rawFrom, "; rawTo: ", rawTo, "; preparedRawFrom: ", preparedRawFrom, "; preparedRawTo: ", preparedRawTo)

		from, errFrom := prepareDate(preparedRawFrom)

		if errFrom != nil {
			return timeIntervals, errors.New("time from is invalid")
		}

		to, errTo := prepareDate(preparedRawTo)

		if errTo != nil {
			return timeIntervals, errors.New("time to is invalid")
		}

		//fmt.Fprintln(outf, "validateSyntaxAndPrepare STEP 2 >> from: ", from, "; to: ", to)

		timeIntervals = append(timeIntervals, TimeInterval{from: from, to: to})
	}

	sort.Slice(timeIntervals, func(i, j int) bool {
		return timeIntervals[i].from.Before(timeIntervals[j].from)
	})

	return timeIntervals, nil
}

func prepareDate(str string) (time.Time, error) {
	t, err := time.Parse(time.RFC3339, str)

	return t, err
}

func prepareStringDate(raw string) string {
	return fmt.Sprintf("2023-08-15T%s.000Z", raw)
}

// (StartDate1 <= EndDate2) and (StartDate2 <= EndDate1)
func validateIntervals(intervals []TimeInterval) bool {
	if len(intervals) == 1 {
		return intervals[0].from.Before(intervals[0].to)
	}

	for i := 1; i < len(intervals); i++ {
		startDatePrev := intervals[i-1].from
		endDatePrev := intervals[i-1].to

		startDateNext := intervals[i].from
		endDateNext := intervals[i].to

		if startDatePrev.After(endDatePrev) || startDateNext.After(endDateNext) {
			return false
		}

		if endDatePrev.After(startDateNext) || endDatePrev.Equal(startDateNext) {
			return false
		}

		if startDatePrev.Equal(startDateNext) || endDatePrev.Equal(endDateNext) {
			return false
		}
	}

	return true
}

func main() {
	in := bufio.NewReader(os.Stdin)

	readAndValidateTimeIntervals(in)

	defer outf.Flush()
}
