def primos (lista):
    listaprimo = []
    fim = len(lista)
    for i in range (0, fim):
        try:
            num = int(lista[i])
        except (ValueError, TypeError):
            continue
        primo = True
        if (num < 2):
            primo = False
        elif (num == 2):
            primo = True
        elif (num % 2 == 0):
            primo = False
        else: 
            for ind in range (3, num, 2):
                if (num % ind == 0):
                    primo = False
                    break
        if (primo == True):
            listaprimo.append(num)
    return listaprimo
       
prim = []
while True:
    nume = (input ("Insira algo para verificar se é um número primo (Quando quiser verificar, basta digitar 'sair': "))
    if (nume == "sair"):
        print (f"Essa é a sua lista {prim}. \n agora vamos verificar quais são primos!")
        break
    else:
        prim.append(nume)
print (f"\nOs números primos da sua lista são: {primos(prim)}")