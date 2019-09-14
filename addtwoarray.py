'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = [str(x+y) for x,y in zip(A,B)]
print(" ".join(C))
