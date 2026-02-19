class pila():
    def __init__(self):
        self.datos=[]
    def agregar(self,dato):
        self.datos.append(dato)
    def quitar(self):
        return self.datos.pop()

PilaNueva = pila()

PilaNueva.agregar("PEDRO")
PilaNueva.agregar("JUAN")
PilaNueva.agregar("LUIS")
PilaNueva.agregar("JAIME")

print(PilaNueva.quitar())
print(PilaNueva.quitar())
print(PilaNueva.quitar())
print(PilaNueva.quitar())


    
