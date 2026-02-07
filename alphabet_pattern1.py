#A 
#A B 
#A B C 
#A B C D 
#A B C D E 

n=int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(j+65),end=" ")
    print()
    