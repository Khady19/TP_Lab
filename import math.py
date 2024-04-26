import math

def calc_distance(point1, point2):

    x1, y1, z1 = point1
    x2, y2, z2 = point2
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    
    return distance

def cal_distance(points1, points2):
    distances = []
    for point1 in points1:
        for point2 in points2:
            distance = calc_distance(point1, point2)
            distances.append(distance)
    return distances

# Test the function
points1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
points2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]
distances = cal_distance(points1, points2)
print("Distances between points:", distances)
