package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

var file string = "../blob.txt"

func privateCounter(file string, xShift int, yShift int) int {
	f, err := os.Open(file)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	total := 0
	var trees []string
	for scanner.Scan() {
		text := scanner.Text()
		trees = append(trees, text)
	}

	x := 0
	y := 0
	x += xShift
	x %= len(trees[0])
	y += yShift
	for y < len(trees) {
		if trees[y][x] == '#' {
			total++
		}
		x += xShift
		x %= len(trees[0])
		y += yShift
	}
	return total
}

func treeCounter(file string) int {

	return (
		privateCounter(file, 1, 1) *
		privateCounter(file, 3, 1) *
		privateCounter(file, 5, 1) *
		privateCounter(file, 7, 1) *
		privateCounter(file, 1, 2))
}

func main() {
	fmt.Println(treeCounter(file))
}
