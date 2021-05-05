tiles = []
x = 296
x_nodes = []
x_change = 63

y = 615
y_nodes = []
y_change = 63

for i in range(10):
    x_nodes.append(x)
    x += x_change

for i in range(10):
    y_nodes.append(y)
    y -= y_change

# for n in range(11):
#     tiles.append([(n, n+1, (x, y))])
#     x += 63

# n = 0
# for i in y_nodes:
#     for j in x_nodes:
#         tiles.append((n, n+1, (j, i)))
#         n+=1

n = 0
left = True
for i in range(10):
    if left:
        for j in range(10):
            tiles.append((n, n+1, (x_nodes[j], y_nodes[i])))
            n+=1
        
        left = False
    else:
        for j in range(9, -1, -1):
            tiles.append((n, n+1, (x_nodes[j], y_nodes[i])))
            n+=1
        left = True

# print(x_nodes)
# print(y_nodes)

from pprint import pprint
print(tiles)