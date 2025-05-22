import math

def sphereSurfaceCollide(sphere, surface):
    point = subPoints(sphere.position, surface.position)
    point = rotatePoint(point, -surface.angle)
    p2 = (clamp(point[0], -surface.size / 2, surface.size / 2), clamp(point[1], -surface.thickness / 2, surface.thickness / 2))
    return dist(point, p2) <= sphere.radius

def sphereSphereCollide(sphere1, sphere2):
    return dist(sphere1.position, sphere2.position) <= (sphere1.radius + sphere2.radius)

def rotatePoint(point, angle):
    x, y = point
    cosAngle = math.cos(angle)
    sinAngle = math.sin(angle)
    return (x * cosAngle - y * sinAngle, x * sinAngle + y * cosAngle)

def addPoints(point1, point2):
    return (point1[0] + point2[0], point1[1] + point2[1])
def subPoints(point1, point2):
    return (point1[0] - point2[0], point1[1] - point2[1])
def clamp(value, minValue, maxValue):
    return max(min(value, maxValue), minValue)
def dist(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
def magnitude(vector):
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2)
def angle(vector):
    return math.atan2(vector[1], vector[0])
def mult(vector, scalar):
    return (vector[0] * scalar, vector[1] * scalar)
def div(vector, scalar):
    return (vector[0] / scalar, vector[1] / scalar)
def normalize(vector):
    mag = magnitude(vector)
    if mag == 0:
        return (0, 0)
    return (vector[0] / mag, vector[1] / mag)
def dot(vector1, vector2):
    return vector1[0] * vector2[0] + vector1[1] * vector2[1]
def cross(vector1, vector2):
    return vector1[0] * vector2[1] - vector1[1] * vector2[0]
def sign(x):
    return (x > 0) - (x < 0)