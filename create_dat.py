import pandas as pd
import os

path = r"D:\Programy\z.studi\ROK 6\magister\full_teddy_excels_plate_values_only"

def create_dat(path):
    for step, name in enumerate(["zebrowa", "szwedler", "lamella"], start=1):
        for elem in os.listdir(path):
            df = pd.read_excel(os.path.join(path, elem))
            lista = [str(par[step]) for par in df.values.tolist()]
            lista.insert(0, df.columns.tolist()[step])
            with open(os.path.join(path[:-35], "teddy_files", name, elem.replace("xlsx", "dat")), "w") as dat_file:
                dat_file.writelines(f"{el}\n" for el in lista if el != "nan")

create_dat(path)