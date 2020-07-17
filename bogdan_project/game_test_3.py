# class Line:
#     def __init__(self):
#         self.a = 123
#
#     def draw(self,h):
#         print(self.a,h)
#
#
# class Point:
#     def __init__(self):
#         self.b = 321
#
# s=Point()
# from random import choice
# ROWS=5
# free_cells=set()
# for i in range(ROWS):
#     for j in range(ROWS):
#         free_cells.add((i, j))
# print(choice(list(free_cells)))
from collections import deque
a=deque()
a.append(1)
a.append(2)
a.append(3)
a=set(a)
print(a)