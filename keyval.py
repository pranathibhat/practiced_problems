d={'a':"Speckbit", 'b':"World", 'c':"Quiet"}
search=input("Search element:")
a=d.items()
for i in a:
    if search==i[1]:
        print("key is ",i[0])
        
