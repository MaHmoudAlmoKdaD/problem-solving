import math
def find_farthest_points(points):
    distance_list = list()
    points_list = list()
    for iterate in range(len(points)):
        coordinates = points[iterate]
        x1 = coordinates[0]
        y1 = coordinates[1]
        for next_point in range(iterate + 1, len(points)):
            next_coordinates = points[next_point]
            x2 = next_coordinates[0]
            y2 = next_coordinates[1]
            distance = math.sqrt( ((x2 - x1) ** 2) + ((y2 - y1) ** 2) )
            points_list.append([(x1, y1), (x2, y2)])
            distance_list.append(distance)
    farthest_apart_points = max(distance_list)
    index = distance_list.index(farthest_apart_points)
    return points_list[index]


points = [(0, 0), (1, 1), (100, 100)]
print(find_farthest_points(points))
# l = [True,True,True,True]
# for i in range(len(l)):
#     l[i] = [(3, 3), (3,3)]
# print(l)