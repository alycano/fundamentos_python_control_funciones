# Aprendiz: Aly Santiago Cano
# Tema: Control de bucles con break, continue y else

print("--- Revision Tecnica de Componentes ---")

componentes = ["Monitor", "Teclado", "ERROR", "Mouse", "Cables"]

for item in componentes:
    if item == "ERROR":
        print("Se detecto un componente defectuoso. Saltando...")
        continue  # Salta el error y sigue con el siguiente
    
    if item == "Cables":
        print("Revision detenida por falta de tiempo.")
        break  # Detiene el bucle por completo
        
    print(f"Revisando: {item} -> Estado OK")
else:
    # Este solo sale si el bucle termina sin un 'break'
    print("Revision finalizada con exito.")