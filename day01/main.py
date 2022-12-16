class Elf:
    def __init__(self, inventory):
        self.inventory = inventory
    
    def getTotalCalories(self):
        return sum(self.inventory)

def read_input(filename):
    payload = []
    file = open(filename, "r")
    raw = file.read()
    file.close()
    raw = raw.split("\n\n")
    for item in raw:
        foods = item.split("\n")
        foods = [int(food) for food in foods]
        elf = Elf(foods)
        payload.append(elf)
    return payload

def getMostCalories(elves):
    return max([elf.getTotalCalories() for elf in elves])

def getTopThreeTotalCalories(elves):
    sorted_elves = sorted(elves, key=lambda elf: elf.getTotalCalories(), reverse=True)
    return sum([sorted_elves[i].getTotalCalories() for i in range(3)])

def main():
    elves = read_input("./input.txt")
    mostCalories = getMostCalories(elves)
    print("Most calories:", mostCalories) # 69836
    topThreeTotalCalories = getTopThreeTotalCalories(elves) 
    print("Top 3 total calories:", topThreeTotalCalories) # 207968


if __name__ == "__main__":
    main()