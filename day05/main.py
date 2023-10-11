from pprint import pprint

def load_data():
    data = []
    with open("input.txt") as f:
        batch = []
        while True:
            line = f.readline()
            if line == "\n":
                data.append(batch)
                batch = []
            if not line:
                data.append(batch)
                break
            batch.append(line.strip())
    return data


def format_preset(preset):
    for i in range(len(preset)):
        s = preset[i]
        s = s.replace('[',' ')
        s = s.replace(']',' ')
        s = s.replace('    ','   .')
        s = s.replace(' ','')
        preset[i] = s
    preset.reverse()
    pprint(preset)
    #---
    yard = {}
    for y in range(1, len(preset)): #Starts on 1 to skip numerics.
        for x in range(len(preset[y])):
            key = x+1
            if key not in yard.keys():
                yard[key] = []
            if preset[y][x] == '.':
                continue
            yard[key].append(preset[y][x])
    pprint(yard)
    return yard


def format_instructions(instructions):
    instructions = list(filter(None, instructions)) #Removing empty lines from list.
    payload = []
    for line in instructions:
        x = line.split()
        payload.append([int(x[1]), int(x[3]), int(x[5])])
    return payload


def move(yard, amount, origin, dest, preserve=False):
    buffer = []
    for i in range(amount):
        buffer.append(yard[origin].pop())
    if preserve:
        buffer.reverse()
    yard[dest].extend(buffer)


def apply_instructions(yard, instructions, preserve):
    for instr in instructions:
        move(yard, instr[0], instr[1], instr[2], preserve)
    

def top_of_each(yard):
    payload = ""
    for i in range(1, len(yard.keys())+1):
        payload += yard[i][-1]
    return payload


def main():
    for i in [0,1]:
        preset, instr = load_data()
        yard = format_preset(preset)
        instructions = format_instructions(instr)
        apply_instructions(yard, instructions, i)
        print("Answer", i+1, ":", top_of_each(yard))
    

if __name__ == "__main__":
    main()
    
    
    
#p1:VWLCWGSDQ
#p2:TCGLQSLPW