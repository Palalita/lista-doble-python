import csv
from graphviz import Digraph


# Nodo AVL
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1


# Árbol AVL
class AVL:
    def __init__(self):
        self.raiz = None

    # Obtener altura
    def altura(self, nodo):
        return nodo.altura if nodo else 0

    # Balance
    def balance(self, nodo):
        return self.altura(nodo.izq) - self.altura(nodo.der)

    # Rotación derecha
    def rotar_derecha(self, y):
        x = y.izq
        T2 = x.der

        x.der = y
        y.izq = T2

        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))
        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))

        return x

    # Rotación izquierda
    def rotar_izquierda(self, x):
        y = x.der
        T2 = y.izq

        y.izq = x
        x.der = T2

        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))
        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))

        return y

    # Insertar
    def insertar(self, nodo, valor):
        if not nodo:
            return Nodo(valor)

        if valor < nodo.valor:
            nodo.izq = self.insertar(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self.insertar(nodo.der, valor)
        else:
            return nodo

        nodo.altura = 1 + max(self.altura(nodo.izq), self.altura(nodo.der))

        balance = self.balance(nodo)

        # Rotaciones
        if balance > 1 and valor < nodo.izq.valor:
            return self.rotar_derecha(nodo)

        if balance < -1 and valor > nodo.der.valor:
            return self.rotar_izquierda(nodo)

        if balance > 1 and valor > nodo.izq.valor:
            nodo.izq = self.rotar_izquierda(nodo.izq)
            return self.rotar_derecha(nodo)

        if balance < -1 and valor < nodo.der.valor:
            nodo.der = self.rotar_derecha(nodo.der)
            return self.rotar_izquierda(nodo)

        return nodo

    # Buscar
    def buscar(self, nodo, valor):
        if not nodo:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self.buscar(nodo.izq, valor)
        else:
            return self.buscar(nodo.der, valor)

    # Obtener mínimo
    def min_valor(self, nodo):
        while nodo.izq:
            nodo = nodo.izq
        return nodo

    # Eliminar
    def eliminar(self, nodo, valor):
        if not nodo:
            return nodo

        if valor < nodo.valor:
            nodo.izq = self.eliminar(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self.eliminar(nodo.der, valor)
        else:
            if not nodo.izq:
                return nodo.der
            elif not nodo.der:
                return nodo.izq

            temp = self.min_valor(nodo.der)
            nodo.valor = temp.valor
            nodo.der = self.eliminar(nodo.der, temp.valor)

        nodo.altura = 1 + max(self.altura(nodo.izq), self.altura(nodo.der))

        balance = self.balance(nodo)

        # Rotaciones
        if balance > 1 and self.balance(nodo.izq) >= 0:
            return self.rotar_derecha(nodo)

        if balance > 1 and self.balance(nodo.izq) < 0:
            nodo.izq = self.rotar_izquierda(nodo.izq)
            return self.rotar_derecha(nodo)

        if balance < -1 and self.balance(nodo.der) <= 0:
            return self.rotar_izquierda(nodo)

        if balance < -1 and self.balance(nodo.der) > 0:
            nodo.der = self.rotar_derecha(nodo.der)
            return self.rotar_izquierda(nodo)

        return nodo

    # Cargar CSV
    def cargar_csv(self, ruta):
        try:
            with open(ruta, newline='') as archivo:
                lector = csv.reader(archivo)
                for fila in lector:
                    for valor in fila:
                        self.raiz = self.insertar(self.raiz, int(valor))
            print("✔ Datos cargados correctamente")
        except Exception as e:
            print("Error:", e)
            
    # Graphviz
    def graficar(self):
        dot = Digraph()

        def agregar(nodo):
            if nodo:
                dot.node(str(nodo.valor))
                if nodo.izq:
                    dot.edge(str(nodo.valor), str(nodo.izq.valor))
                    agregar(nodo.izq)
                if nodo.der:
                    dot.edge(str(nodo.valor), str(nodo.der.valor))
                    agregar(nodo.der)

        agregar(self.raiz)
        dot.render("arbol_avl", view=True, format="png")


# -------------------------
# CLI
# -------------------------
def menu():
    arbol = AVL()

    while True:
        print("\n--- MENÚ AVL ---")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Cargar CSV")
        print("5. Visualizar (Graphviz)")
        print("6. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            valor = int(input("Número: "))
            arbol.raiz = arbol.insertar(arbol.raiz, valor)

        elif opcion == "2":
            valor = int(input("Buscar: "))
            print("✔ Encontrado" if arbol.buscar(arbol.raiz, valor) else "No encontrado")

        elif opcion == "3":
            valor = int(input("Eliminar: "))
            arbol.raiz = arbol.eliminar(arbol.raiz, valor)

        elif opcion == "4":
            ruta = input("Ruta CSV: ")
            arbol.cargar_csv(ruta)

        elif opcion == "5":
            arbol.graficar()

        elif opcion == "6":
            break

        else:
            print("Opción inválida")


# Ejecutar
if __name__ == "__main__":
    menu()