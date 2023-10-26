def iniciar(user,password):
    if(user=="NecroMax" and password == "20062006"):
        print("Feliz bienvenida" , user)
        return True
    else:
        print("usuario invalido")
        return False
if __name__=="__main__":
    persona = input("user")
    cpu =input("password")
    iniciar(persona,cpu)
