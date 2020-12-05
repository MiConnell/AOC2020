package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func fileReader(file string) []string {

	f, err := os.Open(file)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()
	var ret []string
	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		ret = append(ret, scanner.Text())
	}

	return ret
}

func found(a int64, list []int64) bool {
	for _, b := range list {
		if b == a {
			return true
		}
	}
	return false
}

func seatFinder(s []string) int64 {
	var seats []int64

	for _, s := range s {
		s = strings.Replace(strings.Replace(
			strings.Replace(
				strings.Replace(
					s, "F", "0", -1),
				"B", "1", -1),
			"L", "0", -1),
			"R", "1", -1)
		intS, err := strconv.ParseInt(s, 2, 64)

		if err != nil {
			log.Fatal(err)
		}

		seats = append(seats, intS)
	}

	for _, b := range seats {
		fmt.Println(found(b, seats))
		if !found(b, seats) {
			return b
		}
	}
	return 0
}

func main() {
	fmt.Println(seatFinder(fileReader("./blob.txt")))
}
