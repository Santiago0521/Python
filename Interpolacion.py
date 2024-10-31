def calcular_diferencias_divididas(valores_x, valores_y):
    n = len(valores_x)
    coeficientes = [0] * n
    
    for i in range(n):
        coeficientes[i] = valores_y[i]
    
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coeficientes[i] = (coeficientes[i] - coeficientes[i-1]) / (valores_x[i] - valores_x[i-j])
    
    return coeficientes

def construir_polinomio_interpolacion(valores_x, coeficientes):
    n = len(valores_x)
    interpolacion = str(coeficientes[0])
    for i in range(1, n):
        termino = str(coeficientes[i])
        for j in range(i):
            termino += "*(x - " + str(valores_x[j]) + ")"
        interpolacion += " + " + termino
    return interpolacion

# Ingresar los coeficientes manualmente
num_valores = int(input("Por favor, ingresa el número de puntos (grado del polinomio + 1): "))
valores_x = []
valores_y = []

print("Ahora, ingresa los valores de x y y:")
for i in range(num_valores):
    valor_x = float(input(f"Valor de x_{i}: "))
    valor_y = float(input(f"Valor de y_{i}: "))
    valores_x.append(valor_x)
    valores_y.append(valor_y)

coeficientes = calcular_diferencias_divididas(valores_x, valores_y)
polinomio = construir_polinomio_interpolacion(valores_x, coeficientes)

print("Los coeficientes son:", coeficientes)
print("El polinomio de interpolación es:", polinomio)
