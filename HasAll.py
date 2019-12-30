# Program checks for alphaNumeric, alphabetical, digit, lower and upperCase Character in a String
# Using built-in functions for all operations

if __name__ == '__main__':
    s = input()
    a = b = c = d = e = False

    for x in s:
        if(x.isalnum()):
            a = True
        if(x.isalpha()):
            b = True
        if(x.isdigit()):
            c = True
        if(x.islower()):
            d = True
        if(x.isupper()):
            e = True
        if( a ==b and b == c and c == d and d == e):
            exit

print(a)
print(b)
print(c)
print(d)
print(e)
