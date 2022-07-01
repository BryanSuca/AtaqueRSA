import hashlib
import random
# exponenciación modular.
# Devuelve (x^y) % p
def exponenciacionModular(x, y, p):
    r = 1;
    x = x % p;

    while (y > 0):
         
        
        if (y & 1):
            r = (r * x) % p;
        y = y>>1; 
        x = (x * x) % p;
     
    return r;
 
# MiillerRabin
def miillerRabin(d, n):
    #número aleatorio en [2..n-2], el caso cumple n>4
    a = 2 + random.randint(1, n - 4);
 
    #Calculando a^d % n
    x = exponenciacionModular(a, d, n);
 
    if (x == 1 or x == n - 1):
        return True;
 
    #Sigue elevando x al cuadrado mientras uno de los siguiente casos no cumpla
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;
 
        if (x == 1):
            return False;
        if (x == n - 1):
            return True;

    return False;

def calcularPrimo(n,k):
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;
 
    d = n - 1;
    while (d % 2 == 0):
        d //= 2;
 
    # Repite k veces
    for i in range(k):
        if (miillerRabin(d, n) == False):
            return False;
 
    return True;

def randoms(d):
    
    a = random.getrandbits(d)
    if a % 2 == 0:
        a -= 1
    return a

def maximocd(a,b):
    r = b%a
    while r != 0:
        b=a
        a=r
        r= b%a
    return a

def calculae(ø):
    e=2
    le=[]
    while e>1 and e<ø and e<100 :
      if maximocd(e,ø)==1:
        le.append(e)
        e=e+1
      else:
        e=e+1
    print("\nVALORES PARA (e)="+str(le))
    e=int(input("\n\tValor de (e)="))
    while maximocd(e,ø)!=1:
      print("\n\tEliga un valor de la lista !!!")
      e=int(input("\n\tValor de (e)="))
    return e
  
    
def encontrarD(e,φ):
	k=1
	m=(1+(k)*(φ))%(e)
	while m!=0:
		k=k+1
		m=(1+(k)*(φ))%(e)
	d=int((1+(k)*(φ))/(e))
	return d

if __name__ == '__main__':
  s = 4
  bits = 12

  p = randoms(bits)
  q = randoms(bits)

  while not calcularPrimo(p, s):
      p = randoms(bits)
  while not calcularPrimo(q, s):
      q = randoms(bits)  
  if p != q:
      print("Numero primo aleatorio p: " + str(p))
      print("Numero primo aleatorio q: " + str(q))
 

 # 2.- Calcular n = p * q 
    
  n = p * q
  print("Calculando n: " + str(n))
  if n < 280000:
    print("-----------------VUELVA EJECUTAR EL PROGRAMA ---------------------")
    exit()
# 3.- Calcular φ(n)
  φ = (p-1)*(q-1)
  print("Calculando φ(n): " + str(φ))

# 4.- Generar aleatoriamente e ∈ [2, n − 1], tal que gcd(e, φ(n)) = 1
  print("\n#4 CALCULAMOS (e) ")
  print("\t(e)/  1<e<ø and mcd(e,ø)==1")
  e=calculae(φ)
  print("\t(e)="+str(e))

# 5.- Generar d
  d = encontrarD(e,φ)
  print("Calculando d: " + str(d))
    
# 6.- Llave publica y privada
  publica=[n,e]
  privada=[n,d]
  print("LLave publica " + str(publica) )
  print( "LLave privada " + str(privada))

#  Mensaje 1 cifrado y descifrado
  mensaje1 = hashlib.sha1()
  print (" -------------------------------------------------------------------------------------------- ")
  print (" ----------------------------- PRIMER mensaje cifrado por sha-1 ----------------------------- ")
  print (" -------------------------------------------------------------------------------------------- ")
  mensaje1.update(b"Hola mundo")
  print("Mensaje 1 = Hola mundo ")
  numeros1 = mensaje1.hexdigest()
  decimales1 = (int(numeros1,16))
  print( "Mensaje 1 cifrado en hexadecimales con sha-1, m = " + str(numeros1))
  print( "Mensaje 1 cifrado en decimales con sha-1, m = " + str(decimales1))
  print( "Ya que la siguiente cifra es enorme y no cumple que m ∈ [1,n-1], evaluaremos solo los 3 primeros numeros y los 3 ultimos numeros")
  decimales1_1 = 109499
  print( "El mensaje 1 a evaluar es, m = " + str(decimales1_1))
  cifrar = (decimales1_1**d)%n
  print( "Firma digital Sa(m), σ = " + str(cifrar))
  descifrar = (cifrar**e)%n
  print( "Mensaje descifrado Pa(σ), u = " + str(descifrar))
  if decimales1_1 == descifrar:
    print( " El mensaje 1 y la firma 1 descifrada es el mismo!!")
  else:
    print( " El  mensaje 1 y la firma 1 descifrada no es el mismo :(")

#  Mensaje 2 cifrado y descifrado
  mensaje2 = hashlib.sha1()
  print (" --------------------------------------------------------------------------------------------- ")
  print (" ----------------------------- SEGUNDO mensaje cifrado por sha-1 ----------------------------- ")
  print (" --------------------------------------------------------------------------------------------- ")
  mensaje2.update(b"Bienvenidos")
  print("Mensaje 2 = Bienvenidos ")
  numeros2 = mensaje2.hexdigest()
  decimales2 = (int(numeros2,16))
  print( "Mensaje 1 cifrado en hexadecimales con sha-1, m = " + str(numeros2))
  print( "Mensaje 1 cifrado en decimales con sha-1, m = " + str(decimales2))
  print( "Ya que la siguiente cifra es enorme y no cumple que m ∈ [1,n-1], evaluaremos solo los 3 primeros numero y los 3 ultimos numeros")
  decimales2_2 = 270620
  print( "El mensaje 2 a evaluar es, m = " + str(decimales2_2))
  cifrar2 = (decimales2_2**d)%n
  print( "Firma digital Sa(m), σ = " + str(cifrar2))
  descifrar2 = (cifrar2**e)%n
  print( "Mensaje descifrado Pa(σ), u = " + str(descifrar2))
  if decimales2_2 == descifrar2:
    print( " El mensaje 2 y la firma 2 descifrada es el mismo!!")
  else:
    print( " El  mensaje 2 y la firma 2 descifrada no es el mismo :(")

#  Mensaje 3 cifrado y descifrado
  mensaje3 = hashlib.sha1()
  print (" -------------------------------------------------------------------------------------------- ")
  print (" ----------------------------- TERCER mensaje cifrado por sha-1 ----------------------------- ")
  print (" -------------------------------------------------------------------------------------------- ")
  mensaje3.update(b"saludos")
  print("Mensaje 3 = saludos ")
  numeros3 = mensaje3.hexdigest()
  decimales3 = (int(numeros3,16))
  print( "Mensaje 1 cifrado en hexadecimales con sha-1, m = " + str(numeros3))
  print( "Mensaje 1 cifrado en decimales con sha-1, m = " + str(decimales3))
  print( "Ya que la siguiente cifra es enorme y no cumple que m ∈ [1,n-1], evaluaremos solo los 3 primeros numero y los 3 ultimos numeros")
  decimales3_3 = 101520
  print( "El mensaje 1 a evaluar es, m = " + str(decimales3_3))
  cifrar3 = (decimales3_3**d)%n
  print( "Firma digital Sa(m), σ = " + str(cifrar3))
  descifrar3 = (cifrar3**e)%n
  print( "Mensaje descifrado Pa(σ), u = " + str(descifrar3))
  if decimales3_3 == descifrar3:
    print( " El mensaje 3 y la firma 3 descifrada es el mismo!!")
  else:
    print( " El  mensaje 3 y la firma 3 descifrada no es el mismo :(")
