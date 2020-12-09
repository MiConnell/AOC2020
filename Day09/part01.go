package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"

	"github.com/ernestosuarez/itertools"
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

func solver(s []string, preamble int) string {
	start := 0
	var checklist []int

	for i := s[preamble]; i != s[len(s)-1]; {
		for comb := range itertools.CombinationsStr(s[start:preamble:len(s)-1], 2) {
			first, err := strconv.Atoi(comb[0])
			if err != nil {
				log.Fatal(err)
			}
			second, err := strconv.Atoi(comb[1])
			if err != nil {
				log.Fatal(err)
			}
			checklist = append(checklist, first+second)
		}
		goal, _ := strconv.Atoi(s[preamble])

		found := find(checklist, goal)
		if !found {
			return s[preamble]
		}
		start++
		preamble++
	}

	return "0"
}

func find(slice []int, val int) bool {
	for item := range slice {
		if item == val {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println(solver(fileReader("./blob.txt"), 25))
}

// def solver(s: str, preamble: int) -> int:
//     b = s.splitlines()
//     start = 0
//     while b[preamble] != b[-1]:
//         checklist = [
//             int(f) + int(s) for f, s in itertools.combinations(b[start:preamble], 2)
//         ]
//         if (goal := int(b[preamble])) not in checklist:
//             return goal
//         start += 1
//         preamble += 1
//     return 0
