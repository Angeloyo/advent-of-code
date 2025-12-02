import os

def read_input():
    here = os.path.dirname(__file__)
    #input_path = os.path.join(here, "test_input.txt")
    input_path = os.path.join(here, "input.txt")

    with open(input_path, "r", encoding="utf-8") as f:
        line = f.read().strip()
        ranges = line.split(",")

    return ranges

def divide_str(s, n):
    chunck_size = len(s) // n
    return [ s[i*chunck_size : (i+1)*chunck_size] for i in range(n) ]

def main():
    ranges = read_input()
    print(f"Loaded {len(ranges)} ranges")

    sum = 0

    for myrange in ranges:
        #process all ranges
        start, end = myrange.split("-")

        for i in range(int(start), int(end) + 1):
            i_str = str(i)
            n = len(i_str)
            divisores = [j for j in range(1, n+1) if n % j == 0]
            invalids = set()

            for divisor in divisores:
                if divisor == 1: continue
                divided_str = divide_str(i_str, divisor)
                if len(set(divided_str)) == 1:
                    invalids.add(i)
            
            for invalid in invalids:
                sum += invalid

    print(sum)

if __name__ == "__main__":
    main()