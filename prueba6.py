class Clase:
    atributo_clase = "Hola"
    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia

mi_clase = Clase("Que tal")
mi_clase.atributo_clase
mi_clase.atributo_instancia

# 'Hola'
# 'Que tal'