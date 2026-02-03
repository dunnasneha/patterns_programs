#* * * * * * * * * 
#  * * * * * * * 
#    * * * * * 
#      * * * 
#        * 
n=int(input())
for i in range(n-1):
    for j in range(i):
        print(" ",end=" ")
    for k in range((n-i)*2-3):
        print("*",end=" ")
    print()