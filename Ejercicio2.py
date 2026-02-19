class cola:
    def __init__(self):
        self.datos = []
    def encolar(self,dato):
        self.datos.append(dato)
    
    def desencolar(self):
        return self.datos.pop(0)

Colanueva = cola()

Colanueva.encolar("Juan")
Colanueva.encolar("Pedro")
Colanueva.encolar("Luis")

print(Colanueva.desencolar())
print(Colanueva.desencolar())
print(Colanueva.desencolar())


        
        