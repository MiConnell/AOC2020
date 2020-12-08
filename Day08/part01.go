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

func maxValue(lst []int64) int64 {
	var maximum int64 = 0

	for _, l := range lst {
		if maximum <= l {
			maximum = l
		}
	}

	return maximum

}

func seatChecker(s []string) int64 {
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

	return maxValue(seats)
}

func main() {
	fmt.Println(seatChecker(fileReader("./blob.txt")))
}
