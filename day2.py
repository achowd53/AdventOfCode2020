o1=0
o2=0
l=[] 
for s in open("day2.txt"):
    s=s.strip()
    ran,letter,password = s.split(" ")
    a,b = map(int,ran.split("-"))
    letter = letter[0]
    c=0
    for x in password:
        if x==letter:
            c+=1
    if a<=c<=b:
        o1+=1
    if password[a-1] == letter:
        if password[b-1] != letter:
            o2+=1
    if password[b-1] == letter:
        if password[a-1] != letter:
            o2+=1
print(o1)
print(o2)
