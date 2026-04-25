# Aprendiz: Aly Santiago Cano
# Tema: Argumentos variables (*args, **kwargs) y Docstrings

def generar_reporte_detallado(titulo, *categorias, **detalles):
    """
    Genera un reporte tecnico flexible usando argumentos variables.
    *categorias: Nombres de las secciones del reporte.
    **detalles: Informacion extra (Fecha, Responsable, etc.)
    """
    print(f"REPORTE: {titulo.upper()}")
    print(f"Secciones: {', '.join(categorias)}")
    
    for clave, valor in detalles.items():
        print(f"{clave}: {valor}")

# Ejemplo de uso avanzado
generar_reporte_detallado(
    "Inventario Inicial", 
    "Servidores", "Redes", "Perifericos", 
    Fecha="25/04/2026", 
    Encargado="Aly Santiago Cano"
)