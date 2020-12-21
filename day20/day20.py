import numpy as np; from itertools import product
tiles,edgetotile = {}, __import__("collections").defaultdict(list)
def get_edges(tile):
    tile = __import__("copy").deepcopy(tile)
    return [''.join(['0' if x==0else'1'for x in tile[0]]),''.join('0' if x==0else'1'for x in tile[:,-1]),
            ''.join(['0' if x==0else'1'for x in tile[-1]]),''.join('0' if x==0else'1'for x in tile[:,0])]
def hflip(tile): return np.fliplr(tile)
def vflip(tile): return np.flipud(tile)
def rotate(tile, n=1): return np.rot90(tile, n)
for tile in open("day20.txt").read().split('\n\n'): #For each tile in the input
    lines = tile.splitlines()
    num_tile = int(lines[0].split()[1][:-1])
    tiles[num_tile] = np.array([[0if x=='.'else 1for x in line]for line in lines[1:]])
    for edge in get_edges(tiles[num_tile]):
        edgetotile[edge].append(num_tile)
        edgetotile[edge[::-1]].append(num_tile)
possible_corners = [edgetotile[edge][0] for edge in edgetotile if len(edgetotile[edge])==1]
corners = [num_tile for num_tile in set(possible_corners) if possible_corners.count(num_tile)==4]
print("Part 1:",__import__("functools").reduce(__import__("operator").mul,corners))
grid = [[None]*12 for _ in range(12)] #Setting up Puzzle Grid
grid[0][0],num_tile,tile = corners[0], corners[0], tiles[corners[0]] #Orientate Corner
correct_edges = [i for i,edge in enumerate(get_edges(tile)) if len(edgetotile[edge])==1]
if correct_edges == [0,1]: tiles[num_tile] = rotate(tile) #rotation is clockwise
elif correct_edges == [1,2]: tilex[num_tile] = rotate(tile,2)
elif correct_edges == [2,3]: tiles[num_tile] = rotate(tile,3)
for y in range(1,12): #Set up left edge
    tile_num,tile_edge = grid[y-1][0], get_edges(tiles[grid[y-1][0]])[2]
    next_tile = (set(edgetotile[tile_edge])-{tile_num}).pop()
    grid[y][0],tile,edges = next_tile, tiles[next_tile], get_edges(tiles[next_tile])
    tile = rotate(tile,edges.index(tile_edge)if tile_edge in edges else edges.index(tile_edge[::-1]))
    if get_edges(tile)[0] != tile_edge: tile = hflip(tile)
    tiles[next_tile] = tile
for y,x in product(range(12),range(1,12)): #Fill Out Rest
    num_tile,tile_edge = grid[y][x-1], get_edges(tiles[grid[y][x-1]])[1]
    next_tile = (set(edgetotile[tile_edge])-{num_tile}).pop()
    grid[y][x],tile,edges = next_tile, tiles[next_tile], get_edges(tiles[next_tile])
    tile = rotate(tile, 1+(edges.index(tile_edge)if tile_edge in edges else edges.index(tile_edge[::-1])))
    if get_edges(tile)[3] != tile_edge: tile = vflip(tile)
    tiles[next_tile] = tile
grid = np.concatenate([np.concatenate([tiles[x][1:-1,1:-1] for x in grid[y]],1) for y in range(12)],0)
snek = [(18,0),(0,1),(5,1),(6,1),(11,1),(12,1),(17,1),(18,1),(19,1),(1,2),(4,2),(7,2),(10,2),(13,2),(16,2)] #Seasnakes
def sea(var):return np.sum(var)-sum(15for y,x in product(range(94),range(77))if all(var[y+b][x+a]==1for a,b in snek))
print("Part 2:",min([sea(var) for var in [rotate(grid,n)for n in range(4)]+[rotate(vflip(grid),n)for n in range(4)]]))
