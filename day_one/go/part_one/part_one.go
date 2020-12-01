package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func valInList(num int, list []int) bool {
	for _, b := range list {
		if b == num {
			return true
		}
	}
	return false
}

func checkList() int {
	var strNums []string
	var intNums []int

	f, err := os.Open("./blob.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		strNums = append(strNums, scanner.Text())
	}

	for _, i := range strNums {
		s, err := strconv.Atoi(i)
		if err != nil {
			panic(err)
		}
		intNums = append(intNums, s)
	}

	for _, n := range intNums {
		if valInList(n, intNums) && valInList(2020 - n, intNums) {
			return (2020 - n) * n
		}
	}
	return 0
}

func main() {
	fmt.Println(checkList())
}
