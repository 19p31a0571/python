import random
a=int(input("enter"))
for i in range(11):
    b=random.randint(1,10)
    print(b)
    if(a==b):
       print("yes")
       break
    else:
       print("no")
       break
print()
