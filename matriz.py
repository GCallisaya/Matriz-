def determinante_3x3(a, b, c, d, e, f, g, h, i):
    return (a * (e * i - f * h) -
            b * (d * i - f * g) +
            c * (d * h - e * g))

def matriz_cofactores(a, b, c, d, e, f, g, h, i):
    return [
        [ (e * i - f * h), -(d * i - f * g), (d * h - e * g) ],
        [-(b * i - c * h),  (a * i - c * g), -(a * h - b * g) ],
        [ (b * f - c * e), -(a * f - c * d),  (a * e - b * d) ]
    ]

def matriz_adjunta(cofactores):
    # Transponer la matriz de cofactores
    return list(zip(*cofactores))

def inversa_matriz_3x3(a, b, c, d, e, f, g, h, i):
    det = determinante_3x3(a, b, c, d, e, f, g, h, i)
    if det == 0:
        raise ValueError("La matriz es singular y no tiene inversa")
    
    cofactores = matriz_cofactores(a, b, c, d, e, f, g, h, i)
    adjunta = matriz_adjunta(cofactores)
    
    inversa = [[elem / det for elem in row] for row in adjunta]
    return inversa

def resolver_ecuaciones_3x3(a11, a12, a13, a21, a22, a23, a31, a32, a33, b1, b2, b3):
    A_inv = inversa_matriz_3x3(a11, a12, a13, a21, a22, a23, a31, a32, a33)
    
    # Resolver el sistema multiplicando la inversa por el vector b
    x1 = A_inv[0][0] * b1 + A_inv[0][1] * b2 + A_inv[0][2] * b3
    x2 = A_inv[1][0] * b1 + A_inv[1][1] * b2 + A_inv[1][2] * b3
    x3 = A_inv[2][0] * b1 + A_inv[2][1] * b2 + A_inv[2][2] * b3
    
    return x1, x2, x3

# Ejemplo de uso
a11, a12, a13 = 52, 20, 25
a21, a22, a23 = 30, 50, 20
a31, a32, a33 = 18, 30, 55
b1, b2, b3 = 4800, 5810, 5690

x1, x2, x3 = resolver_ecuaciones_3x3(a11, a12, a13, a21, a22, a23, a31, a32, a33, b1, b2, b3)
print(x1)
print(x2)
print(x3)

