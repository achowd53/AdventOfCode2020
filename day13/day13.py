from sympy.ntheory.modular import crt
lines=open("day13.txt").read().splitlines()
t,buses=int(lines[0]),[int(x) if x!='x' else -1 for x in lines[1].split(",")]
wait=[(bus-t%bus,bus) for bus in buses if bus!=-1]
print("Part 1:",min(wait)[0]*min(wait)[1])
print("Part 2:",crt(*zip(*[(bus,-i) for i,bus in enumerate(buses) if bus!=-1]))[0])
