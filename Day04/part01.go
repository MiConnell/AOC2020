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

func passportValidator(s []string) int64 {
	return 0
}

func main() {
	fmt.Println(passportValidator(fileReader("./blob.txt")))
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
