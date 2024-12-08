#Este programa está diseñado para calcular y mostrar el porcentaje de ventas de diferentes modelos de autos basado en el ingreso total generado por cada modelo

def ingresar_datos_modelos(cantidad_modelos):
    modelos = []
    for x in range(cantidad_modelos):
        modelo = input("Ingrese el modelo del auto: ")
        unidades_vendidas = int(input("Ingrese el número de unidades vendidas: "))
        precio_por_unidad = float(input("Ingrese el precio por unidad del modelo: "))
        ingresos_totales = unidades_vendidas * precio_por_unidad
        modelos.append((modelo, ingresos_totales))
    return modelos

def calcular_porcentajes_ventas(modelos):
    total_ingresos = sum(ingresos_totales for _, ingresos_totales in modelos)
    porcentajes = []
    for modelo, ingresos_totales in modelos:
        porcentaje = (ingresos_totales / total_ingresos) * 100
        porcentajes.append((modelo, porcentaje))
    return porcentajes

def ordenar_porcentajes_ventas(porcentajes):
    n = len(porcentajes)
    for k in range(n):
        for x in range(0, n - k - 1):
            if porcentajes[x][1] < porcentajes[x + 1][1]:
                porcentajes[x], porcentajes[x + 1] = porcentajes[x + 1], porcentajes[x]
    return porcentajes

def imprimir_resultados_ventas(porcentajes_ordenados):
    print("Porcentaje de ventas de modelos de auto de mayor a menor:")
    for modelo, porcentaje in porcentajes_ordenados:
        print(f"El modelo de auto '{modelo}' tiene un porcentaje de ventas de {porcentaje:.2f}%")

def ejecutar_programa():
    cantidad_modelos_str = input("¿Cuántos modelos de autos desea ingresar? ")
    try:
        cantidad_modelos = int(cantidad_modelos_str)
        if cantidad_modelos < 0:
            print("La cantidad de modelos no puede ser negativa.")
            return
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")
        return
    modelos = ingresar_datos_modelos(cantidad_modelos)
    porcentajes = calcular_porcentajes_ventas(modelos)
    porcentajes_ordenados = ordenar_porcentajes_ventas(porcentajes)
    imprimir_resultados_ventas(porcentajes_ordenados)

# Bloque principal
if __name__ == "__main__":
    ejecutar_programa()
