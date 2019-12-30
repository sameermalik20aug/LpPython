# Program to print Welcome design
# n must be an odd number and m should be = 3n

''' EXAMPLE n = 9 and m = 27
    
    ------------.|.------------
    ---------.|..|..|.---------
    ------.|..|..|..|..|.------
    ---.|..|..|..|..|..|..|.---
    ----------WELCOME----------
    ---.|..|..|..|..|..|..|.---
    ------.|..|..|..|..|.------
    ---------.|..|..|.---------
    ------------.|.------------'''  

n,m = input().split() 
n = int(n)
m = int(m)
o =1
for x in range(n):
    if(x < n//2):
        my_string=o*(".|.")
        print(my_string.center(m,'-'))
        o += 2
    elif(x>n//2):
        o -= 2
        my_string2=o*(".|.")
        print(my_string2.center(m,'-'))
    else:
        print("WELCOME".center(m,'-'))    