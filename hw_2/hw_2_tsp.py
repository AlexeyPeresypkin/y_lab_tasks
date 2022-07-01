from pprint import pprint

import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming


def distance_ev(point_1, point_2):
    return ((point_2[0] - point_1[0]) ** 2 + (
            point_2[1] - point_1[1]) ** 2) ** 0.5


def create_matrix_distance(points):
    matrix_distance = []
    for point_1 in points:
        path = []
        for point_2 in points:
            path.append([point_1, point_2])
        matrix_distance.append(path)
    for i in range(len(matrix_distance)):
        for c in range(len(matrix_distance)):
            matrix_distance[i][c] = distance_ev(matrix_distance[i][c][0],
                                                matrix_distance[i][c][1])
    return matrix_distance


def result(travel_path):
    distance = 0
    result = f'{x_1} -> '
    for i in range(1, len(travel_path)):
        distance += distance_ev(points[i-1], points[i])
        result += f'{points[i]}[{distance}] -> '
    distance += distance_ev(points[travel_path[-1]], points[1])
    result += f'{x_1}[{distance}] = {distance}'
    return result


if __name__ == '__main__':
    x_1, x_2, x_3, x_4, x_5 = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]
    points = [x_1, x_2, x_3, x_4, x_5]
    matrix_distance = np.array(create_matrix_distance(points))
    distance_matrix = np.array(matrix_distance)
    travel_path, distance = solve_tsp_dynamic_programming(distance_matrix)
    print(result(travel_path))

