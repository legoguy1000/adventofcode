import re


def convert_item(source, map) -> int:
    source = int(source)
    for item in map:
        d, s, r = item.split(" ")
        d = int(d)
        s = int(s)
        r = int(r)
        # print(f"{d} {s} {r}")
        # print(range(s, s+r, 1))
        if source in range(s, s+r, 1):
            return source - s + d
        # for i in range(0, r, 1):
        #     if source == s + i:
        #         return d + i
    return source


def part1():
    data = []
    with open("5-input.txt", "r") as f:
        lines = f.readlines()
    seeds = re.findall(r"\d+", lines[0])

    ### REAL
    seed_to_soil = [x.strip() for x in lines[3:23]]
    soil_to_fertilizer = [x.strip() for x in lines[25:72]]
    fertilizer_to_water = [x.strip() for x in lines[74:107]]
    water_to_light = [x.strip() for x in lines[109:149]]
    light_to_temp = [x.strip() for x in lines[151:179]]
    temp_to_humidity = [x.strip() for x in lines[181:228]]
    humidity_to_location = [x.strip() for x in lines[230:258]]

    # print(seed_to_soil)
    for seed in seeds:
        soil = convert_item(seed, seed_to_soil)
        # print(soil)
        fert = convert_item(soil, soil_to_fertilizer)
        water = convert_item(fert, fertilizer_to_water)
        light = convert_item(water, water_to_light)
        temp = convert_item(light, light_to_temp)
        humid = convert_item(temp, temp_to_humidity)
        location = convert_item(humid, humidity_to_location)
        data.append(location)
    print("Part 1: {}".format(min(data)))


def part2():
    data = []
    min = None
    with open("5-input.txt", "r") as f:
        lines = f.readlines()
    seeds = re.findall(r"\d+ \d+", lines[0])
    # print(seeds)
    ### SAMPLE
    # seed_to_soil = [x.strip() for x in lines[3:5]]
    # soil_to_fertilizer = [x.strip() for x in lines[7:10]]
    # fertilizer_to_water = [x.strip() for x in lines[12:16]]
    # water_to_light = [x.strip() for x in lines[18:20]]
    # light_to_temp = [x.strip() for x in lines[22:25]]
    # temp_to_humidity = [x.strip() for x in lines[27:29]]
    # humidity_to_location = [x.strip() for x in lines[31:33]]

    ### REAL
    seed_to_soil = [x.strip() for x in lines[3:23]]
    soil_to_fertilizer = [x.strip() for x in lines[25:72]]
    fertilizer_to_water = [x.strip() for x in lines[74:107]]
    water_to_light = [x.strip() for x in lines[109:149]]
    light_to_temp = [x.strip() for x in lines[151:179]]
    temp_to_humidity = [x.strip() for x in lines[181:228]]
    humidity_to_location = [x.strip() for x in lines[230:258]]

    # print(seed_to_soil)
    for seed_info in seeds:
        ss, sr = seed_info.split(" ")
        print(f"Seed Range {ss} {sr}")
        for i in iter(range(0, int(sr), 1)):
            # print(f"Seed: {seed}")
            seed = int(ss) + i
            soil = convert_item(seed, seed_to_soil)
            # print(soil)
            fert = convert_item(soil, soil_to_fertilizer)
            water = convert_item(fert, fertilizer_to_water)
            light = convert_item(water, water_to_light)
            temp = convert_item(light, light_to_temp)
            humid = convert_item(temp, temp_to_humidity)
            location = convert_item(humid, humidity_to_location)
            if min is None or location < min:
                min == location

    print("Part 2: {}".format(min))


part1()
part2()
