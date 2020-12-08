lines = open("day8.txt").read().splitlines()
ops=[]
for line in lines:
    op, val = line.split()
    val=int(val)
    ops.append((op,val))

def accumulator(ops):
    repeat=False
    accumulator=i=0
    ran=set()
    while i<len(ops):
        if i in ran:
            repeat=True
            break
        ran.add(i)
        op,val=ops[i]
        if op=='acc':accumulator+=val
        elif op=='jmp':i+=val-1
        i+=1
    return accumulator, repeat
print("Part 1:",accumulator(ops)[0])

swap={'nop':'jmp','jmp':'nop'}
for i,(op,val) in enumerate(ops):
    if op in ['nop','jmp']:
        acc,rep = accumulator(ops[:i]+[(swap[op],val)]+ops[i+1:])
        if not rep: print("Part 2:",acc)
