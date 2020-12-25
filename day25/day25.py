i,n,(card,door) = 0, 1, map(int,open("day25.txt").read().strip().splitlines())
while n != card: i+=1; n=(n*7)%20201227
print(pow(door, i, 20201227))
