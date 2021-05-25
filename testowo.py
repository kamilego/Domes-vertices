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
    if dif > 0:
        return vert_rota(degree+dif)[a]/vert_rota(degree)[a]
    else:
        return vert_rota(degree)[a]/vert_rota(degree+dif)[a]

path = r"D:\Programy\z.studi\ROK 6\magister\vertices_new\test\vertices.xlsx"
main_path = path[:-14]

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

test = np.array(list(dict_split.values()),dtype=object)
test = np.concatenate(test)
pd.DataFrame(test, columns = ["Position X", "Position Y", "Position Z"]).to_excel(os.path.join(main_path,'OUTPUT.xlsx'), index=False)
