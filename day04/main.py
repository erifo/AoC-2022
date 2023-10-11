
def load_data():
    data = []
    with open("input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            pair = line.strip().split(",")
            payload = []
            for elf in pair:
                section = elf.split("-")
                section = range(int(section[0]), int(section[1])+1)
                payload.append(section)
            data.append(payload)
    return data


def count_containing(data):
    c = 0
    for pair in data:
        if all(x in pair[0] for x in pair[1]):
            c += 1
            continue
        if all(x in pair[1] for x in pair[0]):
            c += 1
    return c


def count_overlapping(data):
    o = 0
    for pair in data:
        for x in pair[0]:
            if x in pair[1]:
                o += 1
                break
    return o


def main():
    data = load_data()
    print(data)
    c = count_containing(data)
    o = count_overlapping(data)
    print(c, o)


if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #p1 = 424
    #p2 = 804