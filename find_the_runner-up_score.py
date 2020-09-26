if __name__ == '__main__':
    n = (input())
    p= (input())
    l=p.split()
    arr = map(int,l)
    arr1=sorted(set([score for score in arr] ))
    print(arr1[-2])
