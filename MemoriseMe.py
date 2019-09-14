'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code her
from collections import Counter
N = input()
B = list(map(int,input().split()))
count = Counter(B)
Q = int(input())
memory = []
for i in range(Q):
    ele = int(input())
    memory.append(ele)
for i in memory:
    if i in count:
        print(count[i])
    else:
        print("NOT PRESENT")
