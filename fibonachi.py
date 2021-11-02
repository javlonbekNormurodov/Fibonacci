elements = int(input("Nechta element: "))
n1, n2 = 0, 1
xisob = 0

if elements <= 0:
   print("Musbat son kiriting!")
elif elements == 1:
   print("Fibonacci: ",elements,":")
   print(n1)
else:
   print("Fibonacci: ")
   while xisob < elements:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       xisob += 1