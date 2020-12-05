part1=0
part2=0

temp_list=[]
seat_IDs=[]
for line in open("day5.txt"):
    line=line.strip()
    temp_list.append(line)
for iden in temp_list:
    row=int(iden[:7].replace('F','0').replace('B','1'), 2)
    col=int(iden[-3:].replace('R','1').replace('L','0'),2)
    seat_IDs.append(row*8+col)
seat_IDs.sort()
part1=seat_IDs[-1]
for ID in range(1,len(seat_IDs)):
    if seat_IDs[ID-1]==seat_IDs[ID]-2:
        part2 = seat_IDs[ID]-1
        break
    
print("Part 1: ",part1)
print("Part 2: ",part2)
