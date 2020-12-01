package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"github.com/ernestosuarez/itertools"
)


func checkList() int {
	var strNums []string
	var intNums []int

	f, err := os.Open("../blob.txt")
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

	for i := range itertools.CombinationsInt(intNums, 3) {
		if i[0] + i[1] + i[2] == 2020 {
			return i[0] * i[1] * i[2]
		}
	}
	return 0
}

func main() {
	fmt.Println(checkList())
}
