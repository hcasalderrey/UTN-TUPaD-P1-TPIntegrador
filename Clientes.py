import random

# Función para generar un diccionario aleatorio de clientes con IDs únicos
def generar_clientes(num_clientes):
    nombres = ["Carlos", "Ana", "Luis", "Maria", "Jose", "Elena", "Pedro", "Laura", "Juan", "Marta"]
    clientes = {}
    for i in range(num_clientes):
        nombre = random.choice(nombres) + str(i)
        id_cliente = random.randint(1, 100)
        while id_cliente in clientes.values():
            id_cliente = random.randint(1, 1000)
        clientes[nombre] = id_cliente
    return clientes