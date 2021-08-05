# Entrada de dados
# foi colocado um map aqui para que o split aceite números inteiros
# se eu colocasse str a conta do processamento não aceitaria pois é uma srt e não um int ou float
x1, y1 = map(int, input('Digite as coordenadas de P1: ').split(','))
x2, y2 = map(int, input('Digite as coordenadas de P2: ').split(','))
# Processamento
d = ((y2 - y1)**2 + (x2 - x1)**2)**0.5
# Saída de dados
print(f'A distância euclidiana é: {d:.2f}')
