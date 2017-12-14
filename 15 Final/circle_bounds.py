#!/usr/bin/env python3

source_data = [
    [1, 1, 2],    # | -1,   3;  -1,   3
    [2, 2, 0.5],  # |1.5, 2.5; 1.5, 2.5
    [-1, -3, 2],  # | -3,   1;  -5,   1
    [5, 2, 1]     # |  4,   6;   1,   3
]


def circle_to_bounding_box(circle):
    x_pos, y_pos, radius = circle
    left_bound = x_pos - radius
    right_bound = x_pos + radius
    top_bound = y_pos + radius
    bottom_bound = y_pos - radius

    return (left_bound, right_bound, top_bound, bottom_bound)


def rects_to_bounding_box(*rects):
    left_bound = min([rect[0] for rect in rects])
    right_bound = max([rect[1] for rect in rects])
    top_bound = max([rect[2] for rect in rects])
    bottom_bound = min([rect[3] for rect in rects])

    return (left_bound, right_bound, top_bound, bottom_bound)


def bounds_to_points(bounds):
    left_bound, right_bound, top_bound, bottom_bound = bounds

    point_0 = (left_bound, bottom_bound)
    point_1 = (left_bound, top_bound)
    point_2 = (right_bound, top_bound)
    point_3 = (right_bound, bottom_bound)

    return (point_0, point_1, point_2, point_3)


def bounding_rect(data):
    bounding_boxes = [circle_to_bounding_box(circle) for circle in data]
    superbox = rects_to_bounding_box(*bounding_boxes)
    return bounds_to_points(superbox)

print(bounding_rect(source_data))
