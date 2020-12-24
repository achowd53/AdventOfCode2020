hex = {"nw":-1+1j, "sw":-1-1j,"ne":1+1j,"se":1-1j,"e":2,"w":-2}
tiles = __import__("collections").defaultdict(bool)
for line in open("day24.txt").read().splitlines():
    c, line = 0, line.replace("e","e ").replace("w","w ").split()
    for dir in line: c += hex[dir]
    tiles[c] = not tiles[c]
print("Part 1:",sum(tiles.values()))
black = set(c for c in tiles if tiles[c])
for _ in range(100):
    all = set(c+dir for dir in hex.values() for c in black)
    to_remove = set(c for c in black if sum(c+adj in black for adj in hex.values()) not in [1,2])
    to_add = set(c for c in all if sum(c+adj in black for adj in hex.values()) == 2)
    black = (black-to_remove)|to_add
print("Part 2",len(black))
