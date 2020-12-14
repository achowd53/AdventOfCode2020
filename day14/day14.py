import collections, itertools
lines = open("day14.txt").read().splitlines()
p1_memory, p2_memory = collections.defaultdict(int), collections.defaultdict(int)
for line in lines:
    if "mask" in line: mask = line.split(" = ")[1]
    else:
        address,value = line.split("] = ")
        address,value = int(address[4:]),int(value)
        p1_memory[address] = (value|int(mask.replace('X','0'),2))&int(mask.replace('X','1'),2)
        address_bit = "0"*(36-len(bin(address)[2:]))+bin(address)[2:]
        address_bit = ["1"if mask[i]=="1"else"X"if mask[i]=="X"else c for i,c in enumerate(address_bit)]
        for possible in[list(i)for i in itertools.product([0,1],repeat=address_bit.count('X'))]:
            address = address_bit[:]
            indices = [i for i in range(36) if address[i]=="X"]
            while possible: address[indices.pop()] = str(possible.pop())
            address = "".join(address)
            p2_memory[int(address)] = value
print("Part 1:",sum(p1_memory.values()),"\nPart 2:",sum(p2_memory.values()))
