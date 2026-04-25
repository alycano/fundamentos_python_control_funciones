# Aprendiz: Aly Santiago Cano
# En este ejercicio estoy probando la logica mas basica de un condicional usando un ejemplo de banco

# Aqui defino las variables iniciales con el dinero que tengo y lo que quiero sacar
saldo = 300
retiro = 500

# Uso el comparador >= para verificar si el saldo me alcanza para el retiro
if saldo >= retiro:
    # Si la condicion se cumple, resto el valor del retiro al saldo total
    saldo -= retiro
    print("Retiro exitoso.")
    # Uso una f-string para mostrar como quedo la cuenta despues del proceso
    print(f"Nuevo saldo: {saldo}")
else:
    # Si el saldo es menor al retiro, el programa salta directamente aqui
    print("Fondos insuficientes.")
    # Le recuerdo al usuario cuanta plata tiene para que sepa por que fallo
    print(f"Saldo actual: {saldo}")