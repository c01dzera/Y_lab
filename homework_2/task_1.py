import itertools

vertex = [(0, 2), (2, 5), (8, 3), (5, 2), (6, 6)]
# vertex_cnt = int(input('Введите количество вершин: '))
vertex_cnt = len(vertex)
# for _ in range(vertex_cnt):
# 	i, j = map(int, input('Введите координаты вершин: ').split())
# 	vertex.append((i, j))
# print(vertex)
numbers_vertex = {j: i for i, j in enumerate(vertex)}
# print(numbers_vertex)

matrix = [[0 for i in range(vertex_cnt)] for j in range(vertex_cnt)]
for i in range(vertex_cnt):
	for j in range(vertex_cnt):
		if vertex[i] != vertex[j]:
			matrix[i][j] = ((vertex[i][0] - vertex[i][1])**2 + (vertex[j][0] - vertex[j][1])**2)**0.5

path = 0
for i in itertools.permutations(vertex[1:]):
	way = [vertex[0]]
	for j in range(len(i)):
		way.append(i[j])
	way.append(vertex[0])
	min_length = 9999999
	length = 0
	for v in range(len(way)-1):
		length += matrix[numbers_vertex[way[v]]][numbers_vertex[way[v+1]]]
	if length < min_length:
		min_length = length
print(min_length)
# for i in range(vertex_cnt):
# 	print()
# 	for j in range(vertex_cnt):
# 		print(matrix[i][j], end=' ')
