import matplotlib.pyplot as plt

a = [1,2,3,4]
b = [11,22,33,44]

plt.plot(a,b, color='blue', linewidth=3, label='linea') #Se le asocian propiedades
plt.legend() 
plt.show() 

#Diagrama de Linea
print("Gráfico de Linea")

#Definimos los datos
x1= [3,4,5,6]
y1= [5,6,3,4]
x2= [2,5,8]
y2= [3,4,3]

#Configuramos las caracteristicas del gráfico
plt.plot(x1,y1, label='Linea 1', linewidth=3, color='blue')
plt.plot(x2,y2, label='Linea 2', linewidth=4, color='green')

#Definir titulos y nombres de ejes

plt.title('Diagrama de Lineas')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

#Mostrar leyenda, cuadricula y figura
plt.legend()
plt.grid() #Cuadricula
plt.show()


#Diagrama de Linea
print("Gráfico de Barras")

#Definimos los datos
x1= [0.25,1.25,2.25,3.25,4.5]
y1= [5,10,30,40,80]
x2= [0.75,1.75,2.75,3.75,4.75]
y2= [42,26,10,29,66]

#Configuramos las caracteristicas del gráfico
plt.bar(x1,y1, label='Datos 1', width=0.5, color='red')
plt.bar(x2,y2, label='Datos 2', width=0.54, color='green')

#Definir titulos y nombres de ejes

plt.title('Diagrama de Barras')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

#Mostrar leyenda, cuadricula y figura
plt.legend()
#plt.grid() #Cuadricula
plt.show()



#Histograma (Para mostrar distribución)
print("Histograma")
#Definimos los datos
a= [10,20,70,70,70,70,40,40,40,60,65,66,66] #Notas
bins= [0,10,20,30,40,50,60,70,80,90,100] 

#Configuramos las caracteristicas del gráfico
plt.hist(a , bins, histtype = 'bar', rwidth=0.5, color='lightgreen')

#Definir titulos y nombres de ejes

plt.title('Histograma')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
#Mostrar figura
plt.show()


#Gráfico de dispersión
print("Gráfico de dispersión")

#Definimos los datos
x1= [0.25,1.25,2.25,3.25,4.5]
y1= [5,10,30,40,80]
x2= [0.75,1.75,2.75,3.75,4.75]
y2= [42,26,10,29,66]

#Configuramos las caracteristicas del gráfico
plt.scatter(x1,y1, label='Datos 1', color='red')
plt.scatter(x2,y2, label='Datos 2', color='green')

#Definir titulos y nombres de ejes

plt.title('Gráfico de Dispersión')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

#Mostrar leyenda, cuadricula y figura
plt.legend()
#plt.grid() #Cuadricula
plt.show()



#Gráfico de dispersión
print("Gráfico Circular")

#Definimos los datos
dormir = [7,8,6,11,7]
comer = [2,3,4,3,2]
trabajar = [7,8,7,2,2]
recreacion = [8,5,7,8,13]
divisiones = [7,2,2,13]
actividades = ['Dormir', 'Comer', 'Trabajar', 'Recreación']
colores = ['red', 'green', 'purple','orange']
#Configuramos las caracteristicas del gráfico
plt.pie(divisiones, labels=actividades, colors=colores,
 startangle=90, shadow=True, explode=(0.1,0,0,0), autopct='%1.1f%%')

#Definir titulos y nombres de ejes

plt.title('Gráfico Circular')
#Mostrar figura
plt.show()
