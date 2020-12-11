from copy import deepcopy
lines=[*map(list,open("day11.txt").read().splitlines())]
r,c=len(lines),len(lines[0])
def adj_part1(seats,y,x):
    return sum(1for yi,xi in[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]if 0<=x+xi<c and 0<=y+yi<r and seats[y+yi][x+xi]=="#")
def adj_part2(seats,y,x):
    count=0
    for yi,xi in[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        cy,cx=y+yi,x+xi
        while 0<=cx<c and 0<=cy<r and seats[cy][cx]==".": cy,cx=cy+yi,cx+xi
        if 0<=cx<c and 0<=cy<r and seats[cy][cx]=="#": count+=1
    return count
def forward_state(seats, part):
    adjs,occ,new = {1:lambda*a:adj_part1(*a),2:lambda*a:adj_part2(*a)}, {1:4, 2:5}, deepcopy(seats)
    for y in range(r):
        for x in range(c):
            if seats[y][x]=="L"and adjs[part](seats,y,x)==0: new[y][x]="#"
            elif seats[y][x]=="#"and adjs[part](seats,y,x)>=occ[part]: new[y][x]="L"
    return new
def run(part):
    board,prev=deepcopy(lines),[]
    while prev!=board:
        prev=deepcopy(board)
        board=forward_state(board, part)
    return sum(line.count('#') for line in board)
print("Part 1:",run(1))
print("Part 2:",run(2))
