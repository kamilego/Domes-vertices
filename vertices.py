import pandas as pd
import numpy as np
import math
import os


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
    test = np.array(list(diction.values()), dtype=object)
    test = np.concatenate(test)
    return test


def create_diction(param):
    ver_list = param.to_numpy()
    ver_list = ver_list[ver_list[:, 2].argsort()]
    dict_split = {}
    num = 0
    for i in range(0, len(ver_list), 20):
        dict_split["list_"+str(num)] = ver_list[i:20+i]
        num += 11.25
    return dict_split


def create_modyfied_excel(np_range_data, path, elem):
    data = pd.DataFrame(np_range_data, columns = ["Position X", "Position Y", "Position Z"])
    writer = pd.ExcelWriter(os.path.join(path[:-13], f"{elem}.xlsx"))
    data.to_excel(writer, index=False)
    writer.save()


path = r"D:\Programy\z.studi\ROK 6\magister\vertices_new\test\vertices.xlsx"
main_path = path[:-14]

df = pd.read_excel(path)
df = df.dropna(axis="columns")

list_of_dif_degree_ratio = [-2, -1, 1, 2]

obj = {}

for elem in list_of_dif_degree_ratio:
    obj[str(elem)] = changed_diction(create_diction(df), elem)

for elem in obj:
    create_modyfied_excel(obj[elem], path, elem)