# Definición de la función principal
def main():
    # Inicialización de la variable de continuación del bucle
    continuar = True
    
    # Bucle principal
    while continuar:
        # Imprimir el encabezado del conversor
        print("Conversor de unidades")
        print("Cantidad a convertir (pies):")
        
        # Leer la entrada del usuario
        entrada = input()
        
        # Verificar si la entrada es 'Q' para salir del programa
        if entrada.upper() == 'Q':
            continuar = False
        else:
            try:
                # Convertir la entrada a un número decimal
                pies = float(entrada)
                
                # Realizar las conversiones de unidades
                pulgadas = pies * 12
                metros = pies / 3.28
                yardas = pies / 3
                
                # Imprimir los resultados de las conversiones
                print("Resultados:")
                print("Distancia en pulgadas:", pulgadas, "pulg.")
                print("Distancia en metros:", metros, "m.")
                print("Distancia en yardas:", yardas, "yd.")
                print("Para salir, introducir 'Q'")
            except ValueError:
                # Manejar el caso en el que la entrada no sea un número decimal
                print("Error: Introduce un número válido o 'Q' para salir")

# Llamar a la función principal si este script se ejecuta directamente
if __name__ == "__main__":
    main()
