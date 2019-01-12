a=input("Enter 1st list:")
b=input("Enter 2nd list:")
list1=[int(i) for i in a.split()]
list2=[int(i) for i in b.split()]
if (set(list1)&set(list2))==set([]):
    print("False")
else:
    print("True1")


        
