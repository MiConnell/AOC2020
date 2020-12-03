package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func passwordValidator() int {

	f, err := os.Open("./blob.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	total := 0
	for scanner.Scan() {
		text := strings.Fields(scanner.Text())
		params := text[0]
		firstIndex, err := strconv.Atoi(strings.Split(params, "-")[0])
		secondIndex, err := strconv.Atoi(strings.Split(params, "-")[1])
		char := strings.Replace(text[1], ":", "", -1)
		password := text[len(text)-1]
		runes := []rune(password)
		if char == string(runes[firstIndex-1]) {
			if string(runes[firstIndex-1]) != string(runes[secondIndex-1]) {
				total++
			}
		}
		if char == string(runes[secondIndex-1]) {
			if string(runes[firstIndex-1]) != string(runes[secondIndex-1]) {
				total++
			}
		}

		if err != nil {
			log.Fatal(err)
		}
	}
	return total
}

func main() {
	fmt.Println(passwordValidator())
}
