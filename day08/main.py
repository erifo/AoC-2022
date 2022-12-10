class Vector2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __add__(self, other):
        return Vector2(self.x+other.x, self.y+other.y)
    
    def __sub__(self, other):
        return Vector2(self.x-other.x, self.y-other.y)
    
    def __mul__(self, other):
        return Vector2(self.x*other.x, self.y*other.y)
    
    def __rmul__(self, other):
        return Vector2(self.x*other, self.y*other)
    
    def __truediv__(self, other):
        return Vector2(self.x/other, self.y/other)
    
    def __floordiv__(self, other):
        return Vector2(self.x//other, self.y//other)


class Tree:
    def __init__(self, height) -> None:
        self.height = height
        self.can_see_edge_towards = [] #Fill with direction vectors after being proven.
        self.counted = False #Until proven true.


def read_input(filename):
    file = open(filename, "r")
    payload = file.readlines()
    file.close()
    return [d.strip() for d in payload]


def init_trees(data):
    trees = {}
    trees["height"] = len(data)
    trees["width"] = len(data[0])
    for y in range(len(data)):
        for x in range(len(data[y])):
            trees[Vector2(x,y)] = Tree(int(data[y][x]))
    return trees


def get_tree_at(trees, position):
    if position not in trees:
        return None
    return trees[position]


def count_visible_trees(trees):
    missions = [
        {   # North
            "a_end": trees["width"],
            "b_start": 0,
            "b_end": trees["height"],
            "b_step": 1,
            "locator": lambda a,b: Vector2(a,b) # Outer:Horizontal, Inner:Vertical
        },
        {   # West
            "a_end": trees["height"],
            "b_start": 0,
            "b_end": trees["width"],
            "b_step": 1,
            "locator": lambda a,b: Vector2(b,a)  # Outer:Vertical, Inner:Horizontal
        },
        {   # South
            "a_end": trees["width"],
            "b_start": trees["height"]-1,
            "b_end": 0,
            "b_step": -1,
            "locator": lambda a,b: Vector2(a,b)
        },
        {   # East
            "a_end": trees["height"],
            "b_start": trees["width"]-1,
            "b_end": 0,
            "b_step": -1,
            "locator": lambda a,b: Vector2(b,a)
        }
    ]

    visible_trees = 0
    for m in missions:
        for a in range(m["a_end"]):
            tallest_so_far = -1
            for b in range(m["b_start"], m["b_end"], m["b_step"]):
                here = m["locator"](a,b)
                tree = get_tree_at(trees, here)
                if tree.height > tallest_so_far:
                    if not tree.counted:
                        tree.counted = True
                        visible_trees += 1
                    tallest_so_far = tree.height
                if tallest_so_far == 9:
                    break

    trees["visible_trees"] = visible_trees
    return trees


def calc_scenic_score(trees, position):
    this_tree = get_tree_at(trees, position)
    score = 1 # Starts at 1 since everything will be multiplied.
    for direction in [Vector2(0,-1), Vector2(-1,0), Vector2(0,1), Vector2(1,0)]:
        distance = 0
        while True:
            other_tree = get_tree_at(trees, position + ((distance+1) * direction))
            if other_tree == None:
                break
            distance += 1
            if other_tree.height >= this_tree.height:
                break
        score *= distance
    return score


def find_top_scenic_score(trees):
    l = [[calc_scenic_score(trees, Vector2(x,y)) for y in range(trees["height"])] for x in range(trees["width"])]
    return max([item for sublist in l for item in sublist]) # Flatten


def debug_print(trees):
    for y in range(trees["height"]):
        for x in range(trees["width"]):
            tree = get_tree_at(trees, Vector2(x,y))
            h = str(tree.height)
            if tree.counted:
                print(" ("+h+")", end="")
            else:
                print("  "+h+" ", end="")
        print("\n", end="")
    print("-"*20)


def main():
    data = read_input("./input.txt")
    trees = init_trees(data)
    trees = count_visible_trees(trees)
    #debug_print(trees)
    print(trees["visible_trees"]) # a == 1669
    print(find_top_scenic_score(trees)) # b == 331344


if __name__ == "__main__":
    main()
