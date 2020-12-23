class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
cups = [int(n) for n in open("day23.txt").read().strip()]
node_dict = {i:Node(i) for i in range(1,1000001)}
for i in range(len(cups)): node_dict[cups[i]].next = node_dict[cups[(i+1)%len(cups)]]
def simulation(count_cups, steps):
    current = node_dict[cups[0]]
    for _ in range(steps):
        picked = current.next
        current.next = current.next.next.next.next
        label = current.value
        while label in [current.value, picked.value, picked.next.value, picked.next.next.value]:
            label = label-1 if label!=1 else count_cups
        destination = node_dict[label]
        picked.next.next.next = destination.next
        destination.next = picked
        current = current.next
simulation(len(cups), 100)
pointer, p1 = node_dict[1], ""
for _ in range(len(cups)-1):
    pointer = pointer.next
    p1 += str(pointer.value)
print("Part 1:",p1)
cups += list(range(10,1000001))
for i in range(len(cups)): node_dict[cups[i]].next = node_dict[cups[(i+1)%len(cups)]]
simulation(1000000, 10000000)
print("Part 2:",node_dict[1].next.value*node_dict[1].next.next.value)
