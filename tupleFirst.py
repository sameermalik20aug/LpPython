if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    integer_tuple = tuple(integer_list)
    hash_result = hash(integer_tuple)
    print(hash_result)

