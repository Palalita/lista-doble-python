import os

def limpiar():
        os.system('clear' if os.name == 'nt' else 'clear')

class operaciones:
    def Binario(self,n):
        if n == 0:
           return "0"
        elif n == 1:
           return "1"
        return self.Binario(n // 2) + str(n%2)
    
    def contardigitos(self,n):
        n = abs(n)
        if n < 10:
            return 1
        return 1 + self.contardigitos(n//10)
    
    def raiz(self,n,candidato=0):
        if candidato*candidato>n:
            return candidato-1
        return self.raiz(n,candidato+1)
    
    def romanodecimal(self, n):
        valores = {
            'I':1,'V':5,'X':10,
            'L':50,'C':100,
            'D':500,'M':1000
        }

        if len(n) == 0:
            return 0
        
        if len(n) ==1:
            return valores[n]
        
        if valores[n[0]] < valores[n[1]]:
            return (valores[n[1]] - valores[n[0]]) + \
                   self.romanodecimal(n[2:])

        else:
            return valores[n[0]] + \
                   self.romanodecimal(n[1:])
    
    def sumaN(self,n):
        if n == 1:
            return 1
        return n + self.sumaN(n-1)

op=0; 
OP = operaciones() 
while op!=6:
    limpiar()
    print("1. CONVERTIR A BINARIO")
    print("2. CONTAR DIGITOS")
    print("3. RAIZ CUADRADA ENTERA")
    print("4. CONVERTIR A DECIMAL DESDE ROMANO")
    print("5. SUMA DE NUMEROS ENTEROS")
    print("6. SALIR \n")
    op = int(input("ESCOGE LA OPCION A TRABAJAR: "))
    limpiar()
    match op:
        case 1:
           print("CONVIERTE A BINARIO")
           Num = int(input("INGRESA EL NUMERO: "))
           res = OP.Binario(Num)
           print(res)
           input("\nPresiona ENTER para continuar...")

        case 2:
            print("CUENTA DIGITOS")
            Num2 = int(input("INGRESA EL NUMERO: "))
            res2 = OP.contardigitos(Num2)
            print(res2)
            input("\nPresiona ENTER para continuar...")
        case 3:
            print("CALCULA LA RAIZ CUADRADA ENTERA")
            Num3 = int(input("INGRESA EL NUMERO: "))
            res3 = OP.raiz(Num3)
            print(res3)
            input("\nPresiona ENTER para continuar...")
        case 4:
            print("CONVIERTE A DECIMAL DESDE ROMANO")
            Num4 = input("INGRESA EL NUMERO EN ROMANO: ")
            res4 = OP.romanodecimal(Num4)
            print(res4)
            input("\nPresiona ENTER para continuar...")
        
        case 5:
            print("SUMA LOS NUMEROS ENTEROS")
            Num5 = int(input("INGRESA EL NUMERO: "))
            res5 = OP.sumaN(Num5)
            print(res5)
            input("\nPresiona ENTER para continuar...")