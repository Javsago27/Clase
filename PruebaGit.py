def buscarMayor(n1, n2, n3):
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
#-----------------------------------------------------------------------------------------------------------------------------------------------
def buscarMenor(n1, n2, n3):
    menor=0
    if(n1>n2):
        if(n1>n3):
            menor=n1
        else:
            menor=n3
    elif(n2>n3):
        menor=n2
    else:
        menor=n3

    print(f"El mayor es {menor}")
#-----------------------------------------------------------------------------------------------------------------------------------------------
    
n1=input("Introduce un numero: ")
n2=input("Introduce otro numero: ")
n3=input("Introduce otro numero: ")

buscarMayor(n1, n2, n3)
buscarMenor(n1, n2, n3)