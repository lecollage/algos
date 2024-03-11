package main

import "fmt"

type LinkedListInput struct {
	id    string
	Next  string
	value int
}

type LinkedList struct {
	Value int
	Next  *LinkedList
}

type List struct {
	head *LinkedList
}

func (l *List) add(value int) {
	newNode := &LinkedList{Value: value}

	if l.head == nil {
		l.head = newNode
		return
	}

	curr := l.head
	for curr.Next != nil {
		curr = curr.Next
	}

	curr.Next = newNode
}

func (l *List) len() int {
	if l.head == nil {
		return 0
	}

	len := 0

	curr := l.head
	for curr.Next != nil {
		curr = curr.Next
		len++
	}

	return len + 1
}

func (l *List) getKthNode(k int) *LinkedList {
	if l.head == nil {
		return nil
	}

	curr := l.head
	for k > 0 {
		curr = curr.Next
		k--
	}

	return curr
}

func printList(node *LinkedList) {
	curr := node
	for curr != nil {
		fmt.Printf("%d ", curr.Value)

		curr = curr.Next

		if curr != nil {
			fmt.Printf("-> ")
		}
	}
	fmt.Println()
}

func ShiftLinkedList(head *LinkedList, rawK int) *LinkedList {
	list := &List{head: head}

	if rawK == 0 {
		return head
	}

	len := list.len()

	if rawK == len {
		return head
	}

	k := rawK

	if rawK < 0 {
		k = k + (len * (int((k * -1) / len)))
		// fmt.Println("STEP 1 k: ", k)
		k = len + k
		// fmt.Println("STEP 2 k: ", k)
	} else {
		k = k - (len * (int(k / len)))
	}

	if k == 0 || k == len {
		return head
	}

	move := len - k

	// fmt.Println("new k: ", k, "; list.len: ", list.len(), "; rawK/list.len(): ", rawK/list.len())

	// fmt.Println("move: ", move, "; k: ", k)

	kNode := list.getKthNode(move - 1)

	// fmt.Println("k node: ")
	// printList(kNode)

	lastNode := list.getKthNode(len - 1)

	// fmt.Println("last node: ")
	// printList(lastNode)

	cutNode := kNode.Next

	kNode.Next = nil

	// get last node
	lastNode.Next = head

	// fmt.Println("result: ")
	// printList(cutNode)

	return cutNode
}

func prepareLinkedList(nodes *[]LinkedListInput) *LinkedList {
	list := &List{}

	for _, node := range *nodes {
		list.add(node.value)
	}

	return list.head
}

func main() {
	nodes := []LinkedListInput{
		{id: "0", Next: "1", value: 0},
		{id: "1", Next: "2", value: 1},
		{id: "2", Next: "3", value: 2},
		{id: "3", Next: "4", value: 3},
		{id: "4", Next: "5", value: 4},
		{id: "5", Next: "", value: 5},
	}

	head := prepareLinkedList(&nodes)

	// printList(head)
	res := ShiftLinkedList(head, -6)
	printList(res)
}
