import os

def read_input():
    here = os.path.dirname(__file__)
    #input_path = os.path.join(here, "test_input.txt")
    input_path = os.path.join(here, "input.txt")

    with open(input_path, "r", encoding="utf-8") as f:
        line = f.read().strip()
        ranges = line.split(",")

    return ranges

def main():
    ranges = read_input()
    print(f"Loaded {len(ranges)} ranges")
    #print("First 5 ranges:", ranges[:5])

    sum = 0

    for myrange in ranges:
        #process all ranges
        start, end = myrange.split("-")
        print(f"start: {start}, end: {end}")

        for i in range(int(start), int(end) + 1):
            #print(i)
            i_str = str(i)
            mid = len(i_str) // 2

            left = i_str[:mid]
            right = i_str[mid:]

            if left == right:
                sum += i


    print(sum)


if __name__ == "__main__":
    main()