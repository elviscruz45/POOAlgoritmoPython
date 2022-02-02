def funcion_decoradora(funcion):
    def funcion():
        print("Este es el último mensaje...")
        print("Este es el primer mensaje ;)")


def zumbido():
	print("Buzzzzzz")

casa = funcion_decoradora(zumbido)

casa()