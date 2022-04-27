a=int(input("enter"))
fl=0
if a==2 or a==3:
   print("prime")
else:
   for i in range(2,a):
      if a%i==0:
        fl=1
        break
if fl==1:
  print("not prime")
else:
  print("prime")
       
 
