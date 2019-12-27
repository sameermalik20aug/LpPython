# Strings are immutable just like tuples
# This program can also be done by first making the string a list adding new element the making it a string again

def mutate_string(string, position, character):
    string = string[:position]+character+string[position+1:]
    
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)