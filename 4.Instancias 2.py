class persona:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def saluda(self,c):
        return f"hola {c.a},me llamo {self.a}"
    
david=persona("David",35)
erika=persona("Erika",32)

print(david.saluda(erika))
