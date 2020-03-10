
Open In Colab
In [0]:
import numpy
f=int(input('Ingrese el valor de fila:')) ## Fila 
n=int(input('Ingrese el valor de columna:')) #Columna
matriz = numpy.zeros((f,n)) #Matriz
x=numpy.zeros((f)) #Vector solucion

vector=numpy.zeros((n))
comp=numpy.zeros((f))
error=[]  

print ('Método de Gauss-Seidel')
print ('Introduce la matriz de coeficientes y el vector solución')
for r in range(0,f):
    for c in range(0,n):
        matriz[(r),(c)]=float(input("Elemento a["+str(r+1)+str(c+1)+"] "))
    vector[(r)]=float(input('b['+str(r+1)+']: '))
itera=int(input("¿Cual es el numero maxìmo de iteraciones? ")) ##interaciones       
print ("Método de Gauss-Seidel")

##Contador 
k=0 
while k < itera:
    suma=0
    k=k+1
    for r in range(0,f):
        suma=0
        for c in range(0,n):
            if (c != r):
                suma=suma+matriz[r,c]*x[c]               
        x[r]=(vector[r]-suma)/matriz[r,r]
        print("x["+str(r)+"]: "+str(x[r]))
        del error[:]

#Comprobación
for r in range(0,f):
        suma=0
        for c in range(0,n):
            suma=suma+matriz[r,c]*x[c]
            comp[r]=suma
            dif=abs(comp[r]-vector[r])
            error.append(dif)
            print("Error en x[",r,"]=",error[r])
        print("iteraciones: " ,k)
        if all( i<=tol for i in error) == True:
         break
        
print("Chao")
