package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func checkList() int {
	var intNums []int

	f, err := os.Open("../blob.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		intText, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatal(err)
		}
		intNums = append(intNums, intText)
	}

	for _, i := range intNums {
		for _, j := range intNums {
			if i+j == 2020 {
				return i * j
			}
		}
	}

	return 0
}

func main() {
	fmt.Println(checkList())
}

// You are scanning the numbers once to read them.

// You read them into a slice of strings, then convert them into a slice of ints.
// It is possible to either scan it directly to an int (and handle the error), or scan to a string,
// and strconv it into an int (and handle the error), then make just the one []int.

// Then you iterate over them all, and scan the entire list for both the first number and 2020-thatNumber.
// You already know the first number is in the list because you're iterating over it, so that's unnecessary.

// So if you remove that, you're iterating over the numbers and then scanning the entire list (potentially)
// by calling valInList(2020-n, intNums).

// Now, since you're both iterating the list and scanning the list, your solution is O(n2) in complexity.
// That is, worst case, it will take time in proportion to the square of the length of the list.
// This can be done in O(n) -- and the second problem in O(n2).

// Because the input size is just 200 numbers, this isn't a big deal at and brute force is a ok,
// especially in a programming competition. This is about knowing your data.

// Doing it your way, if I had a list of []int, I might go something like:

// for _,i := range intNums { for _,j := range intNums { if i + j == 2020 { return i * j } } }
// That's a simple brute force O(n2) solution and decently quick to type without error.

// for competition you might skip handling errors in exchange for speed
