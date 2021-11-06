##############______FIRST METHOD
a = []
for i in range(1000, 3000+1):
    b = str(i)
    if int(b) % 2 == 0:
        a.append(b)
print(",".join(a))

##############_______SECOND METHOD

x = int(input("ENTER 1st NUMBER : "))
y = int(input("ENTER 2st NUMBER : "))
a = []
for i in range(x, y+1):
    b = str(i)
    if int(b) % 2 == 0:
        a.append(b)
print(",".join(a))
