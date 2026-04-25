
# Aprendiz: Aly Santiago Cano
# Tema: Uso de return y multiples valores

# Defino la funcion que va a procesar los costos de mi inventario
def calcular_totales(precios):
    """Calcula el total de la inversion y el promedio de costo por equipo."""
    
    # Uso la funcion sum() para sumar todos los elementos de la lista precios
    total = sum(precios)
    
    # Calculo el promedio dividiendo el total entre la cantidad de elementos (len)
    promedio = total / len(precios)
    
    # Aqui esta el truco: retorno ambos valores separados por coma
    # Python los manda juntos como si fueran un solo paquete (una tupla)
    return total, promedio 

# Uso de la funcion con una lista de precios de ejemplo
costos = [1500, 2300, 800, 4200]

# Al llamar la funcion, pongo dos variables para recibir los dos resultados
# inversion_total recibe el 'total' y costo_medio recibe el 'promedio'
inversion_total, costo_medio = calcular_totales(costos)

# Imprimo los resultados finales
print(f"Inversion total en hardware: ${inversion_total}")

# Uso :.2f para que el promedio solo muestre dos decimales y se vea mas limpio
print(f"Costo promedio por equipo: ${costo_medio:.2f}")