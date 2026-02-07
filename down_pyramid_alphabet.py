#ABCDEFGHI
# ABCDEFG
#  ABCDE
#   ABC
#    A

n=int(input())

for i in range(n):
    print(' '*i,end="")
    for j in range(2*(n-i)-1):
        print(chr(65+j),end='')
    print()