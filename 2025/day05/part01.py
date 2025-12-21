import os

def read_input():
    here = os.path.dirname(__file__)
    #input_path = os.path.join(here, "test_input.txt")
    input_path = os.path.join(here, "input.txt")

    with open(input_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]

    return lines

def main():
    lines = read_input()
    print(f"Loaded {len(lines)} lines")

    i = lines.index("")
    ranges = lines[:i]
    ingredients = lines[i+1:]

    fresh = set()

    # print(f"ranges: {ranges}")
    # print(f"ingredients: {ingredients}")

    for ingredient in ingredients:
        for range in ranges:
            range_split = range.split("-")

            if int(ingredient) >= int(range_split[0]) and int(ingredient) <= int(range_split[1]):
                fresh.add(ingredient)
                # print(f"ingredient {ingredient} is fresh because >= {range_split[0]} and <= {range_split[1]}")

    # print(f"fresh: {fresh}")
    print(f"len(fresh): {len(fresh)}")

if __name__ == "__main__":
    main()