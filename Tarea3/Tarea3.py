from graphviz import Digraph

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ABB:
    def __init__(self):
        self.raiz = None

    # INSERTAR
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar(nodo.izq, valor)
        elif valor > nodo.valor:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar(nodo.der, valor)

    # BUSCAR
    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscar(nodo.izq, valor)
        else:
            return self._buscar(nodo.der, valor)

    # ELIMINAR
    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izq = self._eliminar(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._eliminar(nodo.der, valor)
        else:
            # Caso 1: sin hijos
            if nodo.izq is None and nodo.der is None:
                return None
            # Caso 2: un hijo
            elif nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            # Caso 3: dos hijos
            temp = self._minimo(nodo.der)
            nodo.valor = temp.valor
            nodo.der = self._eliminar(nodo.der, temp.valor)

        return nodo

    def _minimo(self, nodo):
        while nodo.izq:
            nodo = nodo.izq
        return nodo

    # CARGAR DESDE ARCHIVO
    def cargar_desde_archivo(self, ruta):
        try:
            with open(ruta, 'r') as archivo:
                for linea in archivo:
                    numeros = linea.strip().split(',')
                    for num in numeros:
                        if num.strip().isdigit():
                            self.insertar(int(num.strip()))
            print("Datos cargados correctamente.")
        except Exception as e:
            print("Error al cargar archivo:", e)

    # GRAPHVIZ
    def graficar(self):
        dot = Digraph()

        def agregar_nodos(nodo):
            if nodo:
                dot.node(str(nodo.valor))
                if nodo.izq:
                    dot.edge(str(nodo.valor), str(nodo.izq.valor))
                    agregar_nodos(nodo.izq)
                if nodo.der:
                    dot.edge(str(nodo.valor), str(nodo.der.valor))
                    agregar_nodos(nodo.der)

        agregar_nodos(self.raiz)
        dot.render('arbol', view=True, format='png')


# MENÚ INTERACTIVO
def menu():
    arbol = ABB()

    while True:
        print("\n--- MENÚ ABB ---")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Cargar desde archivo")
        print("5. Graficar árbol")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            valor = int(input("Ingrese número: "))
            arbol.insertar(valor)
            print("Insertado.")

        elif opcion == "2":
            valor = int(input("Ingrese número a buscar: "))
            if arbol.buscar(valor):
                print("Encontrado.")
            else:
                print("No encontrado.")

        elif opcion == "3":
            valor = int(input("Ingrese número a eliminar: "))
            arbol.eliminar(valor)
            print("Eliminado.")

        elif opcion == "4":
            ruta = input("Ingrese ruta del archivo (.txt): ")
            arbol.cargar_desde_archivo(ruta)

        elif opcion == "5":
            arbol.graficar()

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()