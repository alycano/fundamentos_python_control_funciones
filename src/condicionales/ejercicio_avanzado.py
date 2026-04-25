# Aprendiz: Aly Santiago Cano
# Aqui estoy practicando la coincidencia de patrones que es lo mas nuevo que vi en la leccion

# Primero imprimo un titulo para que el usuario sepa que esta en el selector
print("Selector de Frutas")

# Aqui pido el nombre de la fruta y de una vez uso .lower() para que 
# no importe si escriben en mayusculas o minusculas, el programa lo entienda igual
fruta = input("Escribe el nombre de una fruta (manzana, naranja, platano): ").lower()

# Uso la estructura match para comparar lo que el usuario guardo en la variable fruta
match fruta:
    # Si lo que escribio coincide exactamente con manzana, entra aqui
    case "manzana":
        print("La fruta es una manzana.")
    
    # Si coincide con naranja, ejecuta esta linea
    case "naranja":
        print("La fruta es una naranja.")
    
    # Si coincide con platano, pues imprime que es un platano
    case "platano":
        print("La fruta es un platano.")
    
    # Este es el caso por defecto (el comodin), si escriben cualquier otra cosa
    # que no este en la lista, el programa no se rompe y avisa que no la conoce
    case _:
        print("Fruta desconocida.")