#    *  
#   * *  
#  * * *  
# * * * *  
#* * * * *  
n=int(input())
for i in range(1,n):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print('*',end=" ")
    print(" ")