# Aprendiz: Aly Santiago Cano
# Tema: Uso de return y multiples valores

def calcular_totales(precios):
    """Calcula el total de la inversion y el promedio de costo por equipo."""
    total = sum(precios)
    promedio = total / len(precios)
    return total, promedio # Retorna una tupla de valores

# Uso de la funcion
costos = [1500, 2300, 800, 4200]
inversion_total, costo_medio = calcular_totales(costos)

print(f"Inversion total en hardware: ${inversion_total}")
print(f"Costo promedio por equipo: ${costo_medio:.2f}")