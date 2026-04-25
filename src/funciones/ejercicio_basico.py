# Ejercicios de funciones por Aly Cano
# Aprendiz: Aly Santiago Cano
# Tema: Definicion de funciones y parametros

def registrar_equipo(nombre, marca, estado="Nuevo"):
    """Registra un equipo en el sistema RegisTech con un estado por defecto."""
    print(f"Equipo: {nombre}")
    print(f"Marca: {marca}")
    print(f"Estado: {estado}")
    print("-------------------------")

# Llamadas a la funcion
print("--- Registro de Inventario ---")
registrar_equipo("Laptop", "Dell Victus 15") # Usa el estado por defecto
registrar_equipo("Monitor", "LG", "Usado") # Sobrescribe el estado