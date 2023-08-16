package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var outG = bufio.NewWriter(os.Stdout)

var hostsGraph map[int][]int

func buildHostsGraph() {
	in := bufio.NewReader(os.Stdin)

	hostsGraph = make(map[int][]int)

	var usersCount, pairsCount int

	fmt.Fscan(in, &usersCount, &pairsCount)

	// initiate an empty graph
	for i := 0; i < usersCount; i++ {
		hostsGraph[i+1] = make([]int, 0)
	}

	for i := 0; i < pairsCount; i++ {
		// read the couple
		var rawHost, rawFriend string
		fmt.Fscan(in, &rawHost, &rawFriend)

		host, hostErr := strconv.Atoi(rawHost)

		if hostErr != nil {
			panic("Invalid host")
		}

		friend, friendErr := strconv.Atoi(rawFriend)

		if friendErr != nil {
			panic("Invalid friend")
		}

		// add host into hostsGraph with the friend
		hostsGraph[host] = append(hostsGraph[host], friend)

		// add friend into hostsGraph with host as a friend
		hostsGraph[friend] = append(hostsGraph[friend], host)
	}

	// for dev only
	for k := 0; k < usersCount; k++ {
		sort.Slice(hostsGraph[k+1], func(i, j int) bool {
			return hostsGraph[k+1][i] < hostsGraph[k+1][j]
		})
	}
}

func buildPossibleFriendsGraph() {

}

func main() {
	buildHostsGraph()

	fmt.Fprintln(outG, "hostsGraph:", hostsGraph)

	buildPossibleFriendsGraph()

	defer outG.Flush()
}
