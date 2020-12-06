filename="day6.txt"
print("Part 1:",sum(len(set(line)-{'\n'}) for line in open(filename).read().split('\n\n')))
print("Part 2:",sum(len(set.intersection(*[set(person) for person in line.split("\n")])) for line in open(filename).read().split('\n\n')))
