from collections import defaultdict, deque
nums = [*map(int,open("day15.txt").read().strip().split(","))]
seen, last = defaultdict(lambda: deque([],maxlen=2)), nums[-1]
for i in range(1,len(nums)+1): seen[nums[i-1]].append(i)
for i in range(i+1,30000001):
    if len(seen[last])<2: last = 0
    else: last = seen[last][-1]-seen[last][-2]
    seen[last].append(i)
    if i == 2020: print("Part 1:",last)
print("Part 2:",last)
