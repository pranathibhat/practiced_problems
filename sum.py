def summer():
    num=int(input("Enter the number of values for sum:"))
    lst=[int(input()) for i in range(num)]
    sum=0
    for i in lst:
        sum=sum+i
    print(sum)



summer()
