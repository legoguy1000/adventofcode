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

func covert_items(source int, datamap []string) int {
	for i := 0; i < len(datamap); i++ {
		fields := strings.Split(datamap[i], " ")
		d, _ := strconv.Atoi(fields[0])
		s, _ := strconv.Atoi(fields[1])
		r, _ := strconv.Atoi(fields[2])
		if source >= s && source < s+r {
			return source - s + d
		}
	}
	return source
}

func main() {
	part1()
	part2()
}

func part1() {

	file, err := os.OpenFile("5-input.txt", os.O_RDONLY, os.ModePerm)
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
	seeds := r.FindAllString(lines[0], -1)
	seed_to_soil := lines[3:23]
	soil_to_fertilizer := lines[25:72]
	fertilizer_to_water := lines[74:107]
	water_to_light := lines[109:149]
	light_to_temp := lines[151:179]
	temp_to_humidity := lines[181:228]
	humidity_to_location := lines[230:258]
	// fmt.Print(seeds)
	data := -1
	for i := 0; i < len(seeds); i++ {
		seed_int, _ := strconv.Atoi(seeds[i])
		soil := covert_items(seed_int, seed_to_soil)
		fert := covert_items(soil, soil_to_fertilizer)
		water := covert_items(fert, fertilizer_to_water)
		light := covert_items(water, water_to_light)
		temp := covert_items(light, light_to_temp)
		humid := covert_items(temp, temp_to_humidity)
		location := covert_items(humid, humidity_to_location)
		// fmt.Println(location)
		if data == -1 || location < data {
			data = location
		}
	}
	fmt.Printf("Part 1: %d \n", data)
}

func part2() {

	file, err := os.OpenFile("5-input.txt", os.O_RDONLY, os.ModePerm)
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
	r, _ := regexp.Compile("\\d+ \\d+")
	seeds := r.FindAllString(lines[0], -1)
	seed_to_soil := lines[3:23]
	soil_to_fertilizer := lines[25:72]
	fertilizer_to_water := lines[74:107]
	water_to_light := lines[109:149]
	light_to_temp := lines[151:179]
	temp_to_humidity := lines[181:228]
	humidity_to_location := lines[230:258]
	// fmt.Print(seeds)
	data := -1
	for i := 0; i < len(seeds); i++ {
		fields := strings.Split(seeds[i], " ")
		ss, _ := strconv.Atoi(fields[0])
		sr, _ := strconv.Atoi(fields[1])
		fmt.Printf("Seed Range: %d %d \n", ss, sr)

		for j := 0; j < sr; j++ {
			seed := ss + j
			soil := covert_items(seed, seed_to_soil)
			fert := covert_items(soil, soil_to_fertilizer)
			water := covert_items(fert, fertilizer_to_water)
			light := covert_items(water, water_to_light)
			temp := covert_items(light, light_to_temp)
			humid := covert_items(temp, temp_to_humidity)
			location := covert_items(humid, humidity_to_location)
			// fmt.Println(seed)
			if data == -1 || location < data {
				data = location
			}
		}
	}
	fmt.Printf("Part 2: %d \n", data)
}
