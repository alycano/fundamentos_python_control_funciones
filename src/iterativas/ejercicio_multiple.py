# Aprendiz: Aly Santiago Cano
# Tema: Bucle while para validacion de datos

print("--- Acceso al Modulo de Inventarios ---")

clave_seguridad = "sena2026"
intento = ""

# Se repite mientras la clave sea incorrecta
while intento != clave_seguridad:
    intento = input("Por favor, ingrese la clave de acceso: ")
    
    if intento != clave_seguridad:
        print("Clave incorrecta. Intente de nuevo.")

print("Acceso concedido al sistema RegisTech.")