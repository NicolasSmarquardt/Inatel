import numpy as np

# Função C(u) para normalização
def C(u):
    return 1 / np.sqrt(2) if u == 0 else 1

# Função para calcular a IDCT
def inverse_DCT(dct_matrix):
    N = 8  # Tamanho da matriz 8x8
    result = np.zeros((N, N))
    
    for x in range(N):
        for y in range(N):
            sum = 0.0
            for u in range(N):
                for v in range(N):
                    sum += C(u) * C(v) * dct_matrix[u, v] * \
                           np.cos((2*x + 1) * u * np.pi / (2 * N)) * \
                           np.cos((2*y + 1) * v * np.pi / (2 * N))
            result[x, y] = 0.25 * sum
    
    # Arredonda o resultado para uma casa decimal
    return np.round(result, 1)

# Matriz DCT quantizada com apenas dois coeficientes
quantized_dct_matrix = np.array([
    [1259.6, 0, 0, 0, 0, 0, 0, 0],
    [-22.6, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
])

# Executa a IDCT na matriz quantizada
reconstructed_image = inverse_DCT(quantized_dct_matrix)

# Exibindo a imagem reconstruída
print(reconstructed_image)