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

	f, err := os.Open("./blob.txt")
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
