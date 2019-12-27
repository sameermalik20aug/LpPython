# program to find names of studets with second highest marks

# taking input in the form of nested lists
l1 = []
l_final = []
for x in range(int(input())):
    name = input()
    score = float(input())
    l2 = [name,score]
    l1.append(l2)

# sorting the list acc to second argument
l1.sort(key = lambda z:z[1])

high = l1[-1][1]
flag = 1

# finding students with second highest marks
while(flag == 1):
    if l1[-1][1] == high:
        l1.remove(l1[-1])
    else:
        for y in range(len(l1)):
            if l1[y][1] == l1[-1][1]:
                l_final.append(l1[y][0])      
            else:
                pass
        flag = 0
l_final.sort()

print(l1)
print(l_final)