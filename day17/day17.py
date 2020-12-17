from collections import defaultdict; from itertools import product
lines = open("day17.txt").read().splitlines()
cubes_p1={(x,y,0)for(y,line),x in product(enumerate(lines),range(len(lines[0])))if line[x]=='#'}
cubes_p2={(x,y,0,0)for(y,line),x in product(enumerate(lines),range(len(lines[0])))if line[x]=='#'}
for _ in range(6):
    adj_p1,adj_p2 = defaultdict(int),defaultdict(int)
    for (x,y,z),a,b,c in product(cubes_p1,[-1,0,1],[-1,0,1],[-1,0,1]):
        if any([a!=b,b!=c,c!=0]): adj_p1[(x+a,y+b,z+c)]+=1
    for (x,y,z,w),a,b,c,d in product(cubes_p2,[-1,0,1],[-1,0,1],[-1,0,1],[-1,0,1]):
        if any([a!=b,b!=c,c!=d,d!=0]): adj_p2[(x+a,y+b,z+c,w+d)]+=1
    cubes_p1 = {cube for cube in cubes_p1 if adj_p1[cube]in[2,3]}|{cube for cube in adj_p1 if adj_p1[cube]==3}
    cubes_p2 = {cube for cube in cubes_p2 if adj_p2[cube]in[2,3]}|{cube for cube in adj_p2 if adj_p2[cube]==3}
print("Part 1:",len(cubes_p1),"\nPart 2:",len(cubes_p2))
