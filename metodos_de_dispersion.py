import math
import pandas as pd

Notas=[9.0, 9.0, 7.5, 7.5, 9.5, 8.6, 8.6, 8.7, 8.2, 8.0, 7.5, 7.5, 7.5, 8.3, 8.7, 8.3, 8.3, 8.6, 2.7, 2.0, 8.8, 8.5, 7.5, 7.7, 7.5, 9.5, 7.7, 7.7, 8.6, 8.4, 9.1, 7.5, 8.6, 2.0, 8.7, 8.5, 8.6]
     #Aqui tenemos el grupo de las notas.
print(Notas)

promedio = round(sum(Notas)) / (len(Notas)) # El promedio.
print("El promedio:", promedio)

rango = max(Notas) - min(Notas) # Pus el rango nomas.
print("El rango:", rango)
print("")

def calcular_varianza(): #definimos cada parte de la varianza.
    return{
        "diferencia":0,
        "cuadrado":0,
    }

datos={}

suma = 0

print("Varianza:")
for objeto in Notas: #Calcular la varianza
    datos[objeto] = calcular_varianza()

    datos[objeto]["diferencia"] = abs((promedio) - objeto)
    datos[objeto]["cuadrado"] = datos[objeto]["diferencia"] **2

    suma += datos[objeto]["cuadrado"]


tabla = pd.DataFrame({ #Crear una tabla con los resultados
    "Notas": Notas
})

tabla["Diferencia"] = (tabla["Notas"] - tabla["Notas"].mean()).abs()

tabla["Cuadrado"] = tabla["Diferencia"] ** 2


print(tabla)
print("")

varianza = suma / len(Notas) #Valor final de la varianza.



desv_estandar = math.sqrt(varianza) #Calcular la desviacion estandar.
Desv_redondear = round(desv_estandar,3) #La redondeamos.
print("La desviacion estandar es:", Desv_redondear)
print("")
coeficiente = (Desv_redondear / promedio) * 100 #calcular el coeficiente de variacion.
coeficiente_redondear = round(coeficiente,3) #lo redondeamos.
print("El coeficiente de variacion es:", coeficiente_redondear,"%")







 