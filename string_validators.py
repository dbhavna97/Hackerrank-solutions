def alphanumeric(s):
    for i in range(len(s)):
        if s[i].isalnum():
            return True
            break
    return False    
def alphabetical(s):
    for i in range(len(s)):
        if s[i].isalpha():
            return True
            break
    return False
def digits(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return True
            break
    return False
def lowercase(s):
    for i in range(len(s)):
        if s[i].islower():
            return True
            break
    return False
def uppercase(s):
    for i in range(len(s)):
        if s[i].isupper():
            return True
            break
    return False


if __name__ == '__main__':
    s = input()
    print(alphanumeric(s))
    print(alphabetical(s))
    print(digits(s))
    print(lowercase(s))
    print(uppercase(s))
