ancho = int(input("ingresar el ancho  del rectangulo "))
altura = int(input("ingresar la altura del rectangulo "))
caract = input(input("ingresar el caracter a utilizar"))



def dibujar(ancho,altura,letra):
    for i in range(ancho):
        for j in range (altura):
            print(letra,end= " ")
        print()

dibujar (ancho,altura,caract)