import collections
import re

lines = [line.strip() for line in open("day7.txt").readlines()]
contains = collections.defaultdict(list)
inside = collections.defaultdict(set)
for line in lines:
    color = line.split(" bags contain ")[0]
    contains[color] = []
    if line.split(" contain ")[1] == "no other bags.":
        continue
    for value,inner in re.findall(r'(\d+) (.+?) bags?[,.]', line):
        contains[color].append((int(value), inner))
        inside[inner].add(color)

contains_gold = set()
def what_has(color):
    for color in inside[color]:
        contains_gold.add(color)
        what_has(color)
what_has("shiny gold")
print("Part 1:",len(contains_gold))

def bags(color):
    return sum(value * (1+bags(inner)) for value,inner in contains[color])
print("Part 2:",bags("shiny gold"))
