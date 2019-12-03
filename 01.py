
def main():
    total_sum = 0
    with open("01data.txt") as data:
        for line in data:
            num = int(line)
            total_sum += num // 3 - 2
    print("total_sum", total_sum)


def main2():
    total_sum = 0
    with open("01data.txt") as data:
        for line in data:
            num = int(line)
            fuel = num // 3 - 2
            total_sum += fuel
            total_sum += fuel_fuel(fuel)
    print("total_sum", total_sum)

def fuel_fuel(fuel):
    total = 0
    cur = fuel
    while cur // 3 - 2 > 0:
        fuel = cur // 3 - 2
        cur = fuel
        total += fuel if fuel > 0 else 0
    return total

if __name__ == "__main__":
    main()
    main2()
