print('\nFigura de "X"\n')

variable1 = 0
columna1 = "---------------------"  # Solo sirve para repetir el bucle 21 veces
columna2 = "--------------------"   # Repite el bucle 20 veces (segunda mitad)
columnares = ""  # Aquí se va construyendo la figura línea por línea


# Primera mitad de la figura (va hacia adelante)
for espacio in columna1:
  variable1 += 1  # Aumentamos la posición (1 a 21)

  # Si la posición actual es una de las deseadas, agregamos un "*"
  if variable1 == 1 or variable1 == 5 or variable1 == 7 or variable1 == 11 or variable1 == 14 or variable1 == 16 or variable1 == 21:
    columnares += "*"
  
  # En estas posiciones específicas, insertamos un salto de línea
  elif variable1 == 6 or variable1 == 12 or variable1 == 18:
    columnares += "\n"
  
  # En el resto, insertamos un espacio
  else:
    columnares += " "

# Segunda mitad de la figura (va hacia atrás)
for espacio in columna2:
  variable1 -= 1  # Bajamos la posición (20 a 1)

  # Misma lógica que antes: agregar "*" en ciertas posiciones
  if variable1 == 1 or variable1 == 5 or variable1 == 7 or variable1 == 11 or variable1 == 14 or variable1 == 16:
    columnares += "*"
  
  # Saltos de línea en los mismos puntos
  elif variable1 == 6 or variable1 == 12 or variable1 == 18:
    columnares += "\n"
  
  else:
    columnares += " "

print(columnares)
print("\nPrograma finalizado\n")
