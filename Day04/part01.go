package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func passportValidator(file string) int {

	f, err := os.Open(file)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	total := 0
	for scanner.Scan() {
		passports := strings.Split(strings.Replace(scanner.Text(), " ", "\n", -1), "\n\n")
		for _, p := range passports {

		}
	}

	return total
}

func main() {
	fmt.Println(passportValidator("./blob.txt"))
}

// def passport_validator(file: str) -> int:
//     total = 0
//     with open(file, "r") as f:
//         passports = f.read().split("\n\n")
//         for p in passports:
//             p = p.replace("\n", " ").strip()
//             check = [a.split(":")[0] for a in p.split(" ")]
//             if "cid" in check:
//                 check.remove("cid")
//             if len(check) > 6:
//                 total += 1
//     return total
