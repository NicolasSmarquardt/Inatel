import numpy as np

def C(u):
    if u == 0:
        return 1 / np.sqrt(2)
    else:
        return 1

def DCT(matrix):
    N = 8  # Tamanho da matriz 8x8
    result = np.zeros((N, N))
    
    for u in range(N):
        for v in range(N):
            sum = 0.0
            for x in range(N):
                for y in range(N):
                    sum += matrix[x, y] * np.cos((2*x + 1) * u * np.pi / (2 * N)) * np.cos((2*y + 1) * v * np.pi / (2 * N))
            result[u, v] = 0.25 * C(u) * C(v) * sum

    return np.round(result,1)

# Configurando para evitar notação científica
np.set_printoptions(suppress=True, precision=1)

# Exemplo de uso:
matrix = np.array([
    [139, 144, 149, 153, 155, 155, 155, 155],
    [144, 151, 153, 156, 159, 156, 156, 156],
    [150, 155, 160, 163, 158, 156, 156, 156],
    [159, 161, 162, 160, 160, 159, 159, 159],
    [159, 160, 161, 162, 162, 155, 155, 155],
    [161, 161, 161, 161, 160, 157, 157, 157],
    [162, 162, 161, 163, 162, 157, 157, 157],
    [162, 162, 161, 161, 163, 158, 158, 158]
])

dct_matrix = DCT(matrix)
print(dct_matrix)
