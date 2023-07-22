#Primeira versão
'''
valores = input().split(" ")
A, B, C = valores

area_triangulo = (float(A) * float(C))/2
area_circulo = 3.14159 * float(C)**2
area_trapezio = ((float(A) + float(B)) * float(C))/2
area_quadrado = float(B)**2
area_retangulo =float(A) * float(B)

print(f'TRIANGULO: {area_triangulo:.3f}')
print(f'CIRCULO: {area_circulo:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')'''

# Versão otimizada
# Recebe os valores separados por espaço e converte para float na mesma linha
A, B, C = map(float, input().split())

area_triangulo = (A * C) / 2
area_circulo = 3.14159 * C ** 2
area_trapezio = ((A + B) * C) / 2
area_quadrado = B ** 2
area_retangulo = A * B

# Utiliza f-string com formatação direta na saída
print(f'TRIANGULO: {area_triangulo:.3f}')
print(f'CIRCULO: {area_circulo:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')
