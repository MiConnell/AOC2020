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
		min, err := strconv.Atoi(strings.Split(params, "-")[0])
		max, err := strconv.Atoi(strings.Split(params, "-")[1])
		char := strings.Replace(text[1], ":", "", -1)
		password := text[len(text)-1]
		if strings.Contains(password, char) && min <= strings.Count(password, char) && strings.Count(password, char) <= max {
			total++
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
