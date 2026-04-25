# Aprendiz: Aly Santiago Cano
# Aqui estoy practicando como manejar mas de dos opciones usando elif

# Defino una variable con la nota para probar el sistema
nota = 87

print("Sistema de Calificaciones")

# Empiezo revisando la condicion mas alta (sobresaliente)
if nota >= 90:
    print("Calificacion: Sobresaliente")

# Si no fue mayor a 90, el programa baja a esta linea para ver si es mayor a 80
elif nota >= 80:
    # Como 87 es mayor a 80, el programa entrara aqui y saltara el resto
    print("Calificacion: Notable")

# Si fuera una nota mas baja, seguiria evaluando este otro rango
elif nota >= 70:
    print("Calificacion: Aprobado")

# El else es para cualquier nota que este por debajo de 70 (el caso final)
else:
    print("Calificacion: Suspenso")