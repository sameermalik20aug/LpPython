# splitting and joining the string

def split_and_join(line):
    list_of_string = list(line.split(" "))
    modified_string = "-".join(list_of_string)
    return modified_string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)