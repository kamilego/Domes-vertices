import os
import numpy as np
import math


path = r"D:\Programy\z.programowanie\test\vertices.xlsx"[:-13]

for num in range(-2,3):
    if num != 0:
        if not os.path.exists(os.path.join(path, f"{num}")):
            os.makedirs(os.path.join(path, f"{num}"))


def z_y(num):
    x = round(math.sin(math.radians(num)),4)
    z = round(math.cos(math.radians(num)),4)*-1
    return x, 0, z

def clockwiseangle_and_distance(point):
    origin = [0, 0]
    refvec = [0, 1]
    # Vector between point and the origin: v = p - o
    vector = [point[0]-origin[0], point[1]-origin[1]]
    # Length of vector: ||v||
    lenvector = math.hypot(vector[0], vector[1])
    # If length is zero there is no angle
    if lenvector == 0:
        return -math.pi, 0
    # Normalize vector: v/||v||
    normalized = [vector[0]/lenvector, vector[1]/lenvector]
    dotprod = normalized[0]*refvec[0] + normalized[1]*refvec[1]     # x1*x2 + y1*y2
    diffprod = refvec[1]*normalized[0] - refvec[0]*normalized[1]     # x1*y2 - y1*x2
    angle = math.atan2(diffprod, dotprod)
    # Negative angles represent counter-clockwise angles so we need to subtract them
    # from 2*pi (360 degrees)
    if angle < 0:
        return 2*math.pi+angle, lenvector
    # I return first the angle because that's the primary sorting criterium
    # but if two vectors have the same angle then the shorter distance should come first.
    return angle, lenvector


def count_lamell(elem):
    x_y = []
    for degree in range(0, 360, 18):
        value = [round(elem[0]*math.cos(math.radians(degree)), 4), round(elem[0]*math.sin(math.radians(degree)), 4), elem[2]]
        x_y.append(value)
    return x_y


len_dict = {}
for num in np.arange(0, 91, 90/8):
    len_dict[num] = z_y(num)

all_list = [list(len_dict[0])]

for elem in list(len_dict.keys())[1:]:
    all_list.extend(count_lamell(len_dict[elem]))

all_list.sort(key=lambda x: x[2], reverse=True)


PARAM = 10
for elem in all_list:
    for i in range(len(elem)):
        elem[i] = round(elem[i]*PARAM, 4)

for i in range(len(all_list)):
    all_list[i] = str(all_list[i]).replace("[", "").replace("]","")

for i in range(len(all_list[:20])):
    all_list[i] = all_list[i] + " fix pp"
