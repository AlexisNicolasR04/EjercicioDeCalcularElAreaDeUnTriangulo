def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo dado su base y altura."""
    return 0.5 * base * altura

def main():
    print("Cálculo del área de un triángulo")
    
    # Solicitar la base y la altura al usuario
    base = float(input("Ingresa la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))
    
    # Calcular el área
    area = calcular_area_triangulo(base, altura)
    
    # Mostrar el resultado
    print(f"El área del triángulo con base {base} y altura {altura} es {area:.2f} unidades cuadradas.")

if __name__ == "__main__":
    main()
