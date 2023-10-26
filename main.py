from login import*
from cachipum import*


def main():
    print("bienvendos")

    persona = input("user")
    cpu =input("password")
    iniciar(persona,cpu)

    if iniciar():
        juguemos_cachipum
    else:
        print("vuelve a ingresar")

if __name__=="__main__":
    main()
