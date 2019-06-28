def swap_case(s):
    a=""
    for i in range(0,len(s)):
        if s[i].isupper():
            a+=s[i].lower()
        elif s[i].islower():
            a+=s[i].upper()
        elif s[i].isspace():
            a+=s[i]
        else:
            a+=s[i]

    return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
