if __name__ == '__main__':
    n = (input())
    p= (input())
    l = p.split()
    integer_list = map(int, l)
    #integer_list=[int(x) for x in l]
    t=tuple(integer_list)
    print(hash(t))
