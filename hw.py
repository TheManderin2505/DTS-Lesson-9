u1 =[10,20,30,40,50,60,70,80,90,100]
l2 = []
l3 = []
ln = len(u1)

inp1 = int(input("k = ? : "))

for i in range(inp1):
    x = u1.pop(0)
    l2.append(x)

for i in range(0,len(l2)):
    for j in range(i,len(l2)):
        if l2[i] < l2[j]:
            l2[i],l2[j] = l2[j],l2[i]


print(l2)

l2 = l2 + u1
print(l2)