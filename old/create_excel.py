import os
import shutil
import numpy as np


list_of_dif_degree_ratio = [-2, -1, 1, 2]
degrees_list = np.arange(0, 91, 11.25)[1:-1]
ar = []
for y in list_of_dif_degree_ratio:
	for x in degrees_list:
		ar.append(f"{x}_{y}")
for i in range(len(ar)):
	ar[i] = ar[i].replace(".",",")

path = r"D:\Programy\z.studi\ROK 6\magister\all_excels\lamella\vertices_lamell.xlsx"

for elem in ar:
    if "lamell" in path:
        shutil.copy(path, os.path.join(path[:-20], f"{elem}.xlsx"))
    else:
        shutil.copy(path, os.path.join(path[:-13], f"{elem}.xlsx"))
