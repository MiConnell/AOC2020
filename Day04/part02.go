package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

var file string = "./blob.txt"

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

func valueChecker(s []string) int64 {
	return 0
}

func passportValidator(s []string) int64 {
	return 0
}

func main() {
	fmt.Println(passportValidator(fileReader(file)))
}

// def value_checker(dct: Dict[str, str]) -> bool:
//     return (
//         1920 <= int(dct["byr"]) <= 2002
//         and 2010 <= int(dct["iyr"]) <= 2020
//         and 2020 <= int(dct["eyr"]) <= 2030
//         and (m1 := re.match(r"^(\d+)(cm|in)$", dct["hgt"]))
//         and (
//             (m1[2] == "cm" and 150 <= int(m1[1]) <= 193)
//             or (m1[2] == "in" and 59 <= int(m1[1]) <= 76)
//         )
//         and re.match("^#[a-f0-9]{6}$", dct["hcl"])
//         and dct["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
//         and re.match("^[0-9]{9}$", dct["pid"])
//     )

// def passport_validator(file: str) -> int:
//     total = 0
//     with open(file, "r") as f:
//         passports = f.read().split("\n\n")
//         for p in passports:
//             p = p.replace("\n", " ").strip()
//             check = [a.split(":") for a in p.split(" ")]
//             passw_dict = {k: v for k, v in check}
//             if passw_dict.keys() >= REQUIRED and value_checker(passw_dict):
//                 total += 1
//     return total
