import os

def read_input():
    here = os.path.dirname(__file__)
    #input_path = os.path.join(here, "test_input.txt")
    input_path = os.path.join(here, "input.txt")

    with open(input_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]

    return lines

def main():
    banks = read_input()
    print(f"Loaded {len(banks)} banks")

    output = 0
    
    for bank in banks:

        print(f"bank: {bank}")

        max_joltage = 0

        for i in range(0, len(bank)-1):
            for j in range(i+1, len(bank)):

                first_battery = bank[i]
                second_battery = bank[j]

                #print(f"{first_battery}{second_battery}")

                joltage = int(str(first_battery)+str(second_battery))

                if joltage > max_joltage:
                    max_joltage = joltage
        
        print(f"max_joltage: {max_joltage}")

        output += max_joltage

    print(f"output: {output}")
    return output

if __name__ == "__main__":
    main()