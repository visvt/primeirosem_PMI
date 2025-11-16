def login (usuario, senha):
    usu = [["admin", 1234], ["funcionario", 4321]]
    for i in usu:
        if (usuario == i[0]):
            if (senha == i[1]):
                return i[0]
        else:
            continue
    return None

def atraso ():
    for i in range (3, -1, -1):
        for e in range (59, -1, -1):
            print (f"{i}:{e}")
    

        
print ("Olá, bem-vindo")
while True:
    tent = 1
    while (tent <= 3):
            user = (input ("Digite seu nome de usuário: "))
            try:
                passw = int (input ("Digite a senha: "))
                resu = login (user, passw)
            except (ValueError):
                print ("Digite somente números na senha")
                continue
            if (resu != None):
                if (resu == "admin"):
                    print ("Olá admin, seja bem-vindo!")
                elif (resu == "funcionario"):
                    print ("Olá funcionário, seja bem-vindo!")
                break
            else:
                rest = 3 - tent
                print (f"Login errado, você tem mais {rest} tentativas")
                tent = tent + 1
    if (tent > 3):
        print ("Sistema bloqueado, aguarde 3 minutos e tente novamente")
        atraso ()
        print ("Tente novamente")



