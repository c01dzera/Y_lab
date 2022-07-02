vertex = []
vertex_cnt = int(input('Введите количество вершин: '))
for _ in range(vertex_cnt):
	i, j = map(int, input('Введите координаты вершин: ').split())
	vertex.append((i, j))
# print(vertex)
matrix = [[0 for i in range(vertex_cnt)] for j in range(vertex_cnt)]
for i in range(vertex_cnt):
	for j in range(vertex_cnt):
		if vertex[i] != vertex[j]:
			matrix[i][j] = ((vertex[i][0] - vertex[i][1])**2 + (vertex[j][0] - vertex[j][1])**2)**0.5

# for i in range(vertex_cnt):
# 	for j in range(vertex_cnt):
# 		print(matrix[i][j], end=' ')
# 	print()