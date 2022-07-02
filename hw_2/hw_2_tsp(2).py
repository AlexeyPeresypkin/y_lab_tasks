from itertools import permutations


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance_ev(point_1, point_2):
    return ((point_2.x - point_1.x) ** 2 +
            (point_2.y - point_1.y) ** 2) ** 0.5


def find_shortest_path(start, points):
    combinations = permutations(points, len(points))
    result = [(start,) + comb + (start,) for comb in combinations]
    distances = []
    for path in result:
        distance = 0
        for i in range(1, len(path)):
            distance += distance_ev(path[i - 1], path[i])
        distances.append(distance)
    index = distances.index(min(distances))
    return result[index]


def result_to_print(points):
    distance = 0
    start = points[0]
    result = f'{start.x, start.y}'
    for i in range(1, len(points)):
        distance += distance_ev(points[i - 1], points[i])
        result += f' -> ({points[i].x}, {points[i].y})[{distance}] '
    result += f'= {distance}'
    return result


if __name__ == '__main__':
    points = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]
    start_point = Point(points[0][0], points[0][1])
    other_points = [Point(point[0], point[1]) for point in points[1:]]
    shortest_path = find_shortest_path(start_point, other_points)
    print(result_to_print(shortest_path))
