search=[input("Enter search element")]
num=int(input("Enter number of elements"))
inn=[input() for i in range(num)]
if(set(search)&set(inn))==set([]):
    print("False")
else:
    print("True")
