package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func treeCounter() int {

	f, err := os.Open("../blob.txt")
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
	x += 3
	x %= len(trees[0])
	y ++
	for y < len(trees) {
		if trees[y][x] == '#' {
			total ++
		}
		x += 3
		x %= len(trees[0])
		y ++
	}

return total
}

func main() {
	fmt.Println(treeCounter())
}
