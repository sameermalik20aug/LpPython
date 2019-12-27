# changing all upper case letters to lower case and vice-versa
# using ord() and chr() built in functions to convert char to ASCII and vice-versa
# 'a' = 97 , 'z'= 122 , 'A' = 65 , 'Z' = 90 and differnce = 32 

def swap_case(s):
    case_changed = ""
    for x in s:
        if(ord(x) in  range(65,91)):
            case_changed += chr(ord(x)+32)
        elif(ord(x) in  range(97,123)):
            case_changed += chr(ord(x)-32)
        else:
            case_changed += x                    
    return case_changed

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)