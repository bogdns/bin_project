from math import acos, sin, pi


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Vector:
    x = 0
    y = 0

    def __init__(self, point1, point2):
        self.x = point2.x - point1.x
        self.y = point2.y - point1.y

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def scal(self, other_vector):
        return self.x * other_vector.x + self.y * other_vector.y

    def mult_vect(self, other_vector):
        return self.x * other_vector.y - self.y * other_vector.x

    def angle(self, other_vector):
        return acos(self.scal(other_vector) / (self.length() * other_vector.length()))

    def coss(self, other_vector):
        return self.scal(other_vector) / (self.length() * other_vector.length())

    def area_of_triangle(self, other_vector):
        return (self.length() * other_vector.length() * sin(self.angle(other_vector))) / 2

    def symbol_mult_vect(self, other_vector):
        if self.x * other_vector.y - self.y * other_vector.x > 0:
            return 1
        else:
            return -1


class Line:
    s3 = 0

    def __init__(self, method, s1, s2, s3=0):
        if method == 0:
            self.A = s1
            self.B = s2
            self.C = s3
        else:
            self.A = s1.y - s2.y
            self.B = s2.x - s1.x
            self.C = -self.A * s1.x - self.B * s1.y

    def resultxyABC(self, point):
        return self.A * point.x + self.B * point.y + self.C

    def intersection(self, other_line):
        if self.A == 0:
            k = self.A / other_line.A
            y = (self.C - k * other_line.C) / (k * other_line.B - self.B)
            x = (-other_line.B * y - other_line.C) / other_line.A
        else:
            k = other_line.A / self.A
            y = (other_line.C - k * self.C) / (k * self.B - other_line.B)
            x = (-self.B * y - self.C) / self.A
        return [x, y]

    def dist(self, point1):
        return abs(self.resultxy(point1) / (self.A ** 2 + self.B ** 2) ** 0.5)


class Section:
    def __init__(self, point1, point2):
        self.A = point1.y - point2.y
        self.B = point2.x - point1.x
        self.C = -self.A * point1.x - self.B * point1.y


class Polygon:
    """
    m_w_p - massive with points
    elem - element
    """

    def __init__(self, m_w_p):  # передается двумерный массив с точками и их координатами
        self.m_w_p = m_w_p

    def area_of_polygon(self):
        area = 0
        # n = int(input())  # кол-во вершин
        # m = [[0, 0] for i in range(n)]
        # for i in range(n):
        #     x, y = map(int, input().split())
        #     m[i][0] = x
        #     m[i][1] = y
        # p = Polygon(m)
        # print(p.area_of_polygon())
        for elem in range(len(self.m_w_p)):
            area += (self.m_w_p[elem - 1][0] * self.m_w_p[elem][1] -
                     self.m_w_p[elem - 1][1] * self.m_w_p[elem][0])
        return abs(area) / 2

    def check_convex(self):  # нужно вводить по порядку обхода
        v1 = Vector(Point(self.m_w_p[-3][0], self.m_w_p[-3][1]),
                    Point(self.m_w_p[-2][0], self.m_w_p[-2][1]))
        v2 = Vector(Point(self.m_w_p[-2][0], self.m_w_p[-2][1]),
                    Point(self.m_w_p[-1][0], self.m_w_p[-1][1]))
        res = v1.symbol_mult_vect(v2)
        for i in range(len(self.m_w_p)):
            v1 = v2
            v2 = Vector(Point(self.m_w_p[i - 1][0], self.m_w_p[i - 1][1]),
                        Point(self.m_w_p[i][0], self.m_w_p[i][1]))
            res1 = v1.symbol_mult_vect(v2)
            if res1 != res:
                return 'NO'
        return 'YES'
