# TP Integrador: Metodos de Busqueda y Ordenamiento. 
#Christian Bustamante
#Hernan Casalderrey
#Comision 6

# Importar las funciones necesarias de los módulos
from Metodos import bubble_sort, quicksort, binary_search
from Clientes import generar_clientes

# Generar un diccionario de clientes
clientes = generar_clientes(101)  # reemplazamos por 99  #llama a la función para generar clientes aleatorios simulando una base de datos
print("Clientes generados:", clientes) #Muestra los clientes generados aleatoriamente
print("-----------------------------------") #Separador visual

# Obtener solo los IDs de los clientes
ids = list(clientes.values())
 
# Ordenar los IDs según el tamaño de la lista
# Si la lista tiene menos de 100 elementos, usar bubble sort; si tiene 100 o más, usar quicksort
# Esto es para optimizar el rendimiento del algoritmo de ordenamiento
if len(ids) <= 100:
    ids_ordenados = bubble_sort(ids)     
else:
    ids_ordenados = quicksort(ids)

print("IDs ordenados:", ids_ordenados)
print("-----------------------------------") #Separador visual

# Realizar una búsqueda binaria de un ID específico
id_buscar = ids_ordenados[25] # Por ejemplo, buscar el ID en el índice 25
indice = binary_search(ids_ordenados, id_buscar)

if indice != -1:
    print(f"El cliente con ID {id_buscar} fue encontrado en el índice {indice} de la lista ordenada.")
else:
    print(f"El cliente con ID {id_buscar} no fue encontrado en la lista.")

# Imprimir el cliente correspondiente al ID encontrado
for nombre, id_cliente in clientes.items():
    if id_cliente == id_buscar:
        print(f"El cliente con ID {id_buscar} es: {nombre}")
        break
else:
    print(f"No se encontró un cliente con ID {id_buscar}.")


