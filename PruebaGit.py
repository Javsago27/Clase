n1=input("Introduce un numero: ")
n2=input("Introduce otro numero: ")
n3=input("Introduce otro numero: ")
mayor=0

if(n1>n2):
    if(n1>n3):
        mayor=n1
    else:
        mayor=n3
elif(n2>n3):
    mayor=n2
else:
    mayor=n3

print(f"El mayor es {mayor}")