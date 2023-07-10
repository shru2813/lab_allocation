L1 = int(input())
L2 = int(input())
L3 = int(input())
n = int(input())
a = L1 - n
b = L2 - n
c = L3 - n

if a <= b and a <= c :
    print("L1")
elif b <= a and b <= c :
    print("L2")
else:
    print("L3")
