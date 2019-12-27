# performing all the major functions of a list in python

N = int(input())
final_list = []
for x in range(N):
    cmd,*args =  input().split()
    elements = list(map(int,args))
    if (cmd == 'insert') :
       final_list.insert(elements[0],elements[1])
    elif(cmd == 'remove'):
        final_list.remove(elements[0])
    elif(cmd == 'sort'):
        final_list.sort()
    elif(cmd == 'print'):
        print(final_list)
    elif(cmd == 'reverse'):
        final_list.reverse()
    elif(cmd == 'pop'):
        final_list.pop()
    elif(cmd == 'append'):
        final_list.append(elements[0])
    else:
        pass                           


