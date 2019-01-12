def filter():
    num=int(input("Enter the number of elements in the list:"))
    lst=[i+1 for i in range(num)]
    print(lst[1::2])

filter()
