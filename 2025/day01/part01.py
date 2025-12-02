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

    curr_dial = 50
    print("The dial starts by pointing at 50")

    password = 0

    for line in lines:
        direction = line[0]
        steps = int(line[1:])

        if direction == "L":
            curr_dial = (curr_dial - steps) % 100
        elif direction == "R":
            curr_dial = (curr_dial + steps) % 100

        if curr_dial == 0:
            password += 1

        print(f"The dial is rotated {line} to point at {curr_dial}")

    print(password)

if __name__ == "__main__":
    main()