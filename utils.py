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
    cos_angle = math.cos(angle)
    sin_angle = math.sin(angle)
    return (x * cos_angle - y * sin_angle, x * sin_angle + y * cos_angle)

def addPoints(point1, point2):
    return (point1[0] + point2[0], point1[1] + point2[1])
def subPoints(point1, point2):
    return (point1[0] - point2[0], point1[1] - point2[1])
def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)
def dist(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)