def print_rangoli(size):
    
    for i in range(n):
        str="-".join(chr(ord('a')+n-j-1) for j in range(i+1))
        print((str+str[::-1][1:]).center(4*n-3,'-'))
    for i in range(n-1):
        str="-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
        print((str+str[::-1][1:]).center(4*n-3,'-'))    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)