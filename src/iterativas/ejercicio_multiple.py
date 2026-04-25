# Aprendiz: Aly Santiago Cano
# Tema: Bucle while para validacion de datos

# Imprimo el titulo del modulo para dar contexto al usuario
print("--- Acceso al Modulo de Inventarios ---")

# Defino la clave correcta y creo una variable vacia para guardar los intentos
clave_seguridad = "sena2026"
intento = ""

# El bucle while se ejecutara "mientras" la condicion sea verdadera.
# En este caso, mientras lo que el usuario escriba sea diferente (!=) a la clave.
while intento != clave_seguridad:
    # Pedimos el dato dentro del bucle para que se actualice la variable 'intento'
    intento = input("Por favor, ingrese la clave de acceso: ")
    
    # Si lo que escribio sigue siendo diferente a la clave, mostramos un error
    if intento != clave_seguridad:
        print("Clave incorrecta. Intente de nuevo.")

# Si el flujo llega aqui, significa que el bucle termino (porque la clave fue correcta)
print("Acceso concedido al sistema RegisTech.")