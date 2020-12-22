from collections import deque; from itertools import islice
play1,play2 = [[int(c) for c in p.splitlines()[1:]]for p in open("day22.txt").read().split('\n\n')]
p1_play1,p2_play1,p1_play2,p2_play2 = deque(play1), deque(play1), deque(play2), deque(play2)
while p1_play1 and p1_play2:
    c1,c2 = p1_play1.popleft(), p1_play2.popleft()
    if c1 > c2: p1_play1.extend([c1,c2])
    else: p1_play2.extend([c2,c1])
print("Part 1:",sum(i*v for i,v in enumerate(list(p1_play1)if p1_play1 else reversed(p1_play2),1)))
def RC(p1,p2):
    seen = set()
    while p1 and p2:
        if(tuple(p1),tuple(p2))in seen: return"player1",p1
        seen.add((tuple(p1),tuple(p2)))
        c1,c2 = p1.popleft(), p2.popleft()
        if len(p1)>=c1 and len(p2)>=c2: win,_ = RC(deque(islice(p1,c1)),deque(islice(p2,c2)))
        else: win = "player1" if c1>c2 else "player2"
        if win=="player1":p1.extend([c1,c2])
        else:p2.extend([c2,c1])
    return(win,p1 if win=="player1"else p2)
print("Part 2:",sum(i * v for i, v in enumerate(reversed(RC(p2_play1,p2_play2)[1]), 1)))
