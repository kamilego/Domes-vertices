import pandas as pd
import numpy as np
import math


def vert_rota(degree):
    a1 = math.cos(math.radians(degree))
    a2 = math.sin(math.radians(degree))
    return a1, a2


def hor_vert_ratio(degree, dif, a):
    if dif > 0:
        return vert_rota(degree+dif)[a]/vert_rota(degree)[a]
    else:
        return vert_rota(degree)[a]/vert_rota(degree+dif)[a]

path = r"D:\Programy\z.studi\ROK 6\magister\vertices_new\test\vertices.xlsx"

df = pd.read_excel(path)
df = df.dropna(axis="columns")

ver_list = df.to_numpy()
ver_list = ver_list[ver_list[:,2].argsort()]

dict_split = {}
degrees_list = np.arange(0, 91, 11.25)

num = 0
for i in range(0, len(ver_list), 20):
    dict_split["list_"+str(num)] = ver_list[i:20+i]
    num += 11.25