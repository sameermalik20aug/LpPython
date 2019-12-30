# Program to find occurences of sequential subString in a given String
# Eg String = ABCDCDC subString = CDC occurences = 2

def count_substring(string, sub_string):
    i = 0 
    j = 0
    while(i<len(string)):
        if(string[i:i+len(sub_string)] == sub_string):
            j += 1
            i += 1
        else:
            i += 1
    return j           

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)