package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
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

func solver(s []string) int64 {
	var seats []int64

	for _, s := range s {
	}

	return 0
}

func main() {
	fmt.Println(solver(fileReader("./blob.txt")))
}
