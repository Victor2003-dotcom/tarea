import math

# Coordenadas dadas
punto1 = (35, 27)
punto2 = (33, 41)

# Función para distancia euclidiana
def distancia_euclidiana(p1, p2):
    return math.sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))

# Función para distancia manhattan
def distancia_manhattan(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))

# Cálculos
euclidiana = distancia_euclidiana(punto1, punto2)
manhattan = distancia_manhattan(punto1, punto2)

# Mostrar resultados
print(f"Punto 1: {punto1}")
print(f"Punto 2: {punto2}")
print(f"Distancia Euclidiana: {euclidiana:.2f}")
print(f"Distancia Manhattan: {manhattan}")

echo "# tarea" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Victor2003-dotcom/tarea.git
git push -u origin main
