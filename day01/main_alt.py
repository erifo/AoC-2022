def readInput(filename):
    payload = []
    with open(filename, "r") as file:
        raw = file.read().split("\n\n")
        for chunk in raw:
            elf = [int(food) for food in chunk.split("\n")]
            payload.append(elf)
        return payload


def getMostCalories(elves):
    return max([sum(elf) for elf in elves])


def getTopThreeTotalCalories(elves):
    sorted_elves = sorted(elves, key=lambda elf: sum(elf), reverse=True)
    return sum([sum(sorted_elves[i]) for i in range(3)])


def main():
    elves = readInput("./test.txt")
    print("Most calories:", getMostCalories(elves)) # 69836
    print("Top 3 total calories:", getTopThreeTotalCalories(elves)) # 207968


if __name__ == "__main__":
    main()