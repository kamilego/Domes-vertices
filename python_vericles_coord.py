import os
import numpy as np
import math


# path = r"D:\Programy\z.programowanie\test\vertices.xlsx"[:-13]
# for num in range(-2,3):
#     if num != 0:
#         if not os.path.exists(os.path.join(path, f"{num}")):
#             os.makedirs(os.path.join(path, f"{num}"))


def clockwiseangle_and_distance(point):
    origin = [0, 0]
    refvec = [0, 1]
    vector = [point[0]-origin[0], point[1]-origin[1]]
    lenvector = math.hypot(vector[0], vector[1])
    if lenvector == 0:
        return -math.pi, 0
    normalized = [vector[0]/lenvector, vector[1]/lenvector]
    dotprod = normalized[0]*refvec[0] + normalized[1]*refvec[1]
    diffprod = refvec[1]*normalized[0] - refvec[0]*normalized[1]
    angle = math.atan2(diffprod, dotprod)
    if angle < 0:
        return 2*math.pi+angle, lenvector
    return angle, lenvector


def coordinates(elem, start=0, end=360):
    x_y = []
    for degree in range(start, end, 18):
        value = [round(elem[0]*math.cos(math.radians(degree)), 4), round(elem[0]*math.sin(math.radians(degree)), 4), elem[2]]
        x_y.append(value)
    return x_y


def z_y(num, multiply=1):
    x = round(math.sin(math.radians(num)),4)
    z = round(math.cos(math.radians(num)),4)*multiply
    return x, 0, z


def vert_cord_list(dome_type, heigh):
    len_dict = {}
    for num in np.arange(0, 91, 90/8):
        len_dict[num] = z_y(num, -1)

    all_list = [list(len_dict[0])]
    if dome_type == "schwedler":
        for elem in list(len_dict.keys())[1:]:
            all_list.extend(coordinates(len_dict[elem]))
    else:
        for num, elem in enumerate(list(len_dict.keys())[1:], start=1):
            if not num % 2:
                all_list.extend(coordinates(len_dict[elem], -9, 360-9))
            else:
                all_list.extend(coordinates(len_dict[elem]))
    all_list.sort(key=lambda x: x[2], reverse=True)
    for elem in all_list:
        for i in range(len(elem)):
            elem[i] = round(elem[i]*heigh, 4)
    return all_list

def print_list(heigh, vert_list):
    for i in range(len(vert_list)):
        vert_list[i] = str(vert_list[i]).replace("[", "").replace("]","")

    for i in range(len(vert_list[:20])):
        vert_list[i] = vert_list[i] + " fix pp"

    for num, i in enumerate(vert_list, start=1):
        print(num, i)


HEIGHT = 10

a = vert_cord_list(("schwedler"), HEIGHT)
print()
b = vert_cord_list(("lamell"), HEIGHT)


def create_diction(vert_list):
    dict_split = {}
    num = 0
    for i in range(0, len(vert_list), 20):
        dict_split["list_"+str(num)] = vert_list[i:20+i]
        num += 11.25
    return dict_split

def vert_rota(degree):
    a1 = math.cos(math.radians(degree)) # degree for X,Y
    a2 = math.sin(math.radians(degree)) # degree for Z
    return a1, a2


def vert_ratio(degree, dif, a):
    # a = 0 == XY
    # a = 1 == Z
    return vert_rota(degree+dif)[a]/vert_rota(degree)[a]


def changed_diction(diction, degree_dif):
    for elem in list(diction.keys())[1:-1]:
        for row in diction[elem]:
            for num in range(3):
                a = 0 if num < 2 else 1
                row[num] = round(row[num]*vert_ratio(float(elem[5:]), degree_dif, a), 4)
    return np.concatenate(np.array(list(diction.values()), dtype=object))

obj = {}
for elem in range(-2,3):
    obj[str(elem)] = changed_diction(create_diction(a), elem)


