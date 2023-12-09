package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	part1()
	part2()
}

func part1() {
	file, err := os.OpenFile("6-input.txt", os.O_RDONLY, os.ModePerm)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	lines := []string{}
	sc := bufio.NewScanner(file)
	for sc.Scan() {
		lines = append(lines, sc.Text()) // GET the line string
	}
	if err := sc.Err(); err != nil {
		log.Fatalf("scan file error: %v", err)
		return
	}
	r, _ := regexp.Compile("\\d+")
	times := r.FindAllString(lines[0], -1)
	distances := r.FindAllString(lines[1], -1)
	fmt.Println(times)
	fmt.Println(distances)
	data := make([]int, len(times))
	final := 1
	for i := 0; i < len(times); i++ {
		t, _ := strconv.Atoi(times[i])
		d, _ := strconv.Atoi(distances[i])
		for j := 0; j <= t; j++ {
			dist := j * (t - j)
			if dist > d {
				data[i] += 1
			}
		}
		final *= data[i]
	}
	fmt.Printf("Part 1: %d \n", final)
}

func part2() {
	file, err := os.OpenFile("6-input.txt", os.O_RDONLY, os.ModePerm)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	lines := []string{}
	sc := bufio.NewScanner(file)
	for sc.Scan() {
		lines = append(lines, sc.Text()) // GET the line string
	}
	if err := sc.Err(); err != nil {
		log.Fatalf("scan file error: %v", err)
		return
	}
	r, _ := regexp.Compile("\\d+")
	times := r.FindAllString(strings.ReplaceAll(lines[0], " ", ""), -1)
	distances := r.FindAllString(strings.ReplaceAll(lines[1], " ", ""), -1)
	time, _ := strconv.Atoi(times[0])
	distance, _ := strconv.Atoi(distances[0])
	data := 0
	for j := 0; j <= time; j++ {
		dist := j * (time - j)
		if dist > distance {
			data += 1
		}
	}
	fmt.Printf("Part 2: %d \n", data)
}
