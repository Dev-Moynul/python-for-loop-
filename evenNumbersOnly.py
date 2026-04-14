num=int(input())
for x in range(1,num+1):
    if x%2==0:
            print(x,end=" ")


# better solution
n=int(input())
for x in range(2,n+1,2):
      print (x,end=" ")