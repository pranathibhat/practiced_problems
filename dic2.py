d={'a':'Hello','b':'Hey',3:"Hi"}
n=int(input("Enter the number of inputs"))
for i in range(n):
    t=input().split()
    if i!=d.keys():
        d[t[0]]=t[1]
print(d)
