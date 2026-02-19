import os
from graphviz import Digraph
def limpiar():
        os.system('clear' if os.name == 'nt' else 'clear')

class nodo:
    def __init__(self,carnet,nombre,apellido):
        self.carnet = carnet
        self.nombre = nombre
        self.apellido = apellido
        self.sig = None
        self.ant = None

class lista:
    def __init__(self):
        self.inicio = None
        
    
    def agregarinicio(self,nombre,apellido,carnet,): 
        self.nodito = nodo(carnet,nombre,apellido) 
        self.nodito.sig = self.inicio 
        self.inicio = self.nodito
    
    def mostrar(self):

        if self.inicio is None:
            print("None -> None")
            return

        temp = self.inicio
        print("None <- ", end="")
        while temp is not None:
            print(f"[{temp.nombre},{temp.apellido},{temp.carnet}]", end="")     
            if temp.sig is not None:
                print(" <-> ", end="")        
            temp = temp.sig
        print(" -> None")


    def agregarfinal(self,nombre,apellido,carnet):
        self.nodito = nodo(carnet,nombre,apellido) 
        if self.inicio is None:
            self.inicio = self.nodito
            return
        temp = self.inicio
        while temp.sig is not None:
            temp = temp.sig
        
        temp.sig = self.nodito
        self.nodito.ant = temp
    
    def eliminardato(self,carnet):

        if self.inicio is None:
            print("Lista vacia")
            return
        
        temp = self. inicio
        while temp is not None and temp.carnet != carnet:
            temp = temp.sig
        if temp is None:
            print("No se encontro el nodo")
            return
        if temp.ant is None:
            self.inicio = temp.sig
            if self.inicio is not None:
                self.inicio.ant = None
        
        else:
            temp.ant.sig = temp.sig
            if temp.sig is not None:
                temp.sig.ant = temp.ant
        
        print("Nodo eliminado")
            

    def graficar(self):
        dot = Digraph()
        dot.attr(rankdir ='LR')

        temp = self.inicio
        i = 0

        while temp is not None:
            nombre_nodo = f"N{i}"
            etiqueta = f"{temp.nombre}\n{temp.apellido}\n{temp.carnet}"
            dot.node(nombre_nodo, etiqueta)

            if temp.sig is not None:
                dot.edge(nombre_nodo, f"N{i+1}")
                dot.edge(f"N{i+1}", nombre_nodo)
            
            temp = temp.sig
            i+=1
        
        dot.render("lista_doble", view=True, format="png")
op=0;  
act1 = lista()
while op!=6:
    limpiar()
    print("1. INSERTAR VALORES AL PRINCIPIO")
    print("2. INSERTAR VALORES AL FINAL")
    print("3. ELIMINAR POR VALOR")
    print("4. MOSTRAR LA LISTA EN CONSOLA")
    print("5. MOSTRAR LA LISTA EN GRAFICADA")
    print("6. SALIR \n")
    op = int(input("ESCOGE LA OPCION A TRABAJAR: "))
    limpiar()
    match op:
        case 1:
            NOM1 = input("INGRESA EL NOMBRE: ")
            APE1 = input("INGRESA EL APELLIDO: ")
            CARNE1 = int(input("INGRESA EL CARNET: "))
            act1.agregarinicio(NOM1,APE1,CARNE1)
     
        case 2:
            NOM2 = input("INGRESA EL NOMBRE: ")
            APE2 = input("INGRESA EL APELLIDO: ")
            CARNE2 = int(input("INGRESA EL CARNET: "))
            act1.agregarfinal(NOM2,APE2,CARNE2)
        case 3:
            CARNE3 = int(input("INGRESA EL CARNET: "))
            act1.eliminardato(CARNE3)
        case 4:
            act1.mostrar()
            input("\nPresiona ENTER para continuar...")
        
        case 5:
            act1.graficar()
            input("\nPresiona ENTER para continuar...")




