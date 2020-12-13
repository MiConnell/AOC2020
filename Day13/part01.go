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

func solver(s []string) int {
	timestamp, _ := strconv.Atoi(s[0])
	busses := strings.Split(s[1], ",")
	finalTimestamp := timestamp
	var busIDs []int
	maxMod := 0
	currBus := 0
	for _, bus := range busses {
		if bus != "x" {
			b, _ := strconv.Atoi(bus)
			busIDs = append(busIDs, b)
		}
	}
	for _, bus := range busIDs {
		mod := timestamp % bus
		if mod > maxMod {
			maxMod = mod
			currBus = bus
		}
	}
	for i := finalTimestamp; i%currBus != 0; i++ {
		finalTimestamp++
	}

	return (finalTimestamp - timestamp) * currBus
}

func main() {
	fmt.Println(solver(fileReader("./blob.txt")))
}
