import pandas as pd
import numpy as np

path = r"D:\Programy\z.studi\ROK 6\magister\vertices_new\test\vertices.xlsx"

df = pd.read_excel(path)
df = df.dropna(axis="columns")

ver_list = df.to_numpy()
ver_list = ver_list[ver_list[:,2].argsort()]

dict_split = {}

for i in range(0, len(ver_list), 20):
    dict_split["list_"+str(i)] = ver_list[i:20+i]

