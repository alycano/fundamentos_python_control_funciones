# Aprendiz: Aly Santiago Cano
# Tema: Coincidencia de patrones (match-case)

print("Selector de Frutas")
fruta = input("Escribe el nombre de una fruta (manzana, naranja, platano): ").lower()

match fruta:
    case "manzana":
        print("La fruta es una manzana.")
    case "naranja":
        print("La fruta es una naranja.")
    case "platano":
        print("La fruta es un platano.")
    case _:
        print("Fruta desconocida.")