
   # Autor lucif3r : email - anirudh@anirudhanand.com   
   # Este programa ayudará a descifrar texto cifrado a texto sin formato si tiene
   # más de 1 texto cifrado encriptado con el mismo módulo (N) pero diferente
   # exponentes. Usamos el algoritmo de Euclides extendido para lograr esto.
   # Se usara la libreria gmpy2
   # Para instalar gympy en windows abrir el terminal cmd y colocar: pip install gmpy2
import gmpy2
   
   
class RSAModuli:
       def __init__(self):
           self.a = 0
           self.b = 0
           self.m = 0
           self.i = 0
       def gcd(self, num1, num2):
           """
           Esta función se usa para encontrar el MCD de 2 números.
           :parámetro num1:
           :parámetro num2:
           :devolver:
           """
           if num1 < num2:
               num1, num2 = num2, num1
           while num2 != 0:
               num1, num2 = num2, num1 % num2
           return num1
       def extended_euclidean(self, e1, e2):
           """
           El valor a es el inverso multiplicativo modular de e1 y e2.
           b se calcula a partir de la ecuación: (e1*a) + (e2*b) = mcd(e1, e2)
           :param e1: exponente 1
           :param e2: exponente 2
           """
           self.a = gmpy2.invert(e1, e2)
           self.b = (float(self.gcd(e1, e2)-(self.a*e1)))/float(e2)
       def modular_inverse(self, c1, c2, N):
           """
           i es el inverso multiplicativo modular de c2 y N.
           i^-b es igual a c2^b. Entonces, si el valor de b es -ve, tenemos
           tengo que averiguar i y luego hacer i^-b.
           El texto sin formato final viene dado por m = (c1^a) * (i^-b) %N
           :param c1: texto cifrado 1
           :param c2: texto cifrado 2
           :param N: Módulo
           """
           i = gmpy2.invert(c2, N)
           mx = pow(c1, self.a, N)
           my = pow(i, int(-self.b), N)
           self.m= mx * my % N
       def print_value(self):
           print("Mensaje:",self.m)

   
   
def main():
       c = RSAModuli()
       N  = 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667
       c1 = 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516052471686245831933544
       c2 = 35794234179725868774991807832568455403003778024228226193532908190484670252364665786748759822531352444533388184
       e1 = 7
       e2 = 11
       c.extended_euclidean(e1, e2)
       c.modular_inverse(c1, c2, N)
       c.print_value()
    
if __name__ == '__main__':
    main()