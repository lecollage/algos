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

type PossibleFriendsResult struct {
	host            int
	possibleFriends []int
}

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
	results := make([]PossibleFriendsResult, 0)
	for host := range hostsGraph {
		fmt.Fprintln(outG, "buildPossibleFriendsGraph  >> host:", host, hostsGraph[host])

		exceptions := make([]int, 0)
		exceptions = append(exceptions, host)

		for _, friend := range hostsGraph[host] {
			exceptions = append(exceptions, friend)
		}

		results = append(results, getPossibleFriends(hostsGraph[host], host, exceptions))
	}

	sort.Slice(results, func(i, j int) bool {
		return results[i].host < results[j].host
	})

	for _, result := range results {
		res := ""
		if len(result.possibleFriends) > 0 {
			for _, possibleFriend := range result.possibleFriends {
				res += strconv.Itoa(possibleFriend) + " "
			}
		} else {
			res = "0"
		}
		fmt.Fprintln(outG, res)
	}
}

func containsG[T comparable](s []T, e T) bool {
	for _, v := range s {
		if v == e {
			return true
		}
	}
	return false
}

func getPossibleFriends(friends []int, host int, exceptions []int) PossibleFriendsResult {
	var possibleFriendsGraph map[int][]int

	possibleFriendsGraph = make(map[int][]int)

	for _, friend := range friends {
		//fmt.Fprintln(outG, "getPossibleFriends STEP 1 >> friend:", friend)

		for _, possibleFriend := range hostsGraph[friend] {
			//fmt.Fprintln(outG, "getPossibleFriends STEP 2 >> possibleFriend:", possibleFriend, "; hostsGraph[friend]:", hostsGraph[friend])
			if !containsG(exceptions, possibleFriend) {
				_, ok := possibleFriendsGraph[possibleFriend]

				if !ok {
					possibleFriendsGraph[possibleFriend] = make([]int, 0)
				}

				possibleFriendsGraph[possibleFriend] = append(possibleFriendsGraph[possibleFriend], friend)
				//fmt.Fprintln(outG, "getPossibleFriends STEP 3 >> possibleFriendsGraph[possibleFriend]:", possibleFriendsGraph[possibleFriend])
			}
		}
	}

	fmt.Fprintln(outG, "getPossibleFriends STEP 10 >> possibleFriendsGraph for :", host, possibleFriendsGraph)

	// find the max of possible friends
	max := 0
	for _, friends := range possibleFriendsGraph {
		length := len(friends)
		if length > max {
			max = length
		}
	}

	fmt.Fprintln(outG, "getPossibleFriends STEP 11 >> max:", max)

	var possibleFriends = make([]int, 0)

	for possibleFriend, friends := range possibleFriendsGraph {
		length := len(friends)
		if max == length {
			possibleFriends = append(possibleFriends, possibleFriend)
		}
	}

	fmt.Fprintln(outG, "getPossibleFriends STEP 12 >> result:", possibleFriends)

	return PossibleFriendsResult{
		host:            host,
		possibleFriends: possibleFriends,
	}
}

func main() {
	buildHostsGraph()

	fmt.Fprintln(outG, "hostsGraph:", hostsGraph)

	buildPossibleFriendsGraph()

	defer outG.Flush()
}
