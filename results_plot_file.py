import matplotlib.pyplot as plt
import numpy as np
import domes_vertices

def top_bar_value(res):
    for rect in res:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., height, '%d' % int(height), ha='center', va='bottom')

labels = ["Kopuła Żebrowa", "Kopuła Schwedlera", "Kopuła Lamella zakrzywiona"]
displacement = [47.277, 44.707, 46.032]
forces = [948.5, 876.4, 869.0]
num_of_elem = [domes_vertices.dome_1_length, domes_vertices.dome_2_length, domes_vertices.dome_3_length]

bar_x_position = np.arange(len(labels))
width = 0.1

fig, ax = plt.subplots()
res1 = ax.bar(bar_x_position - width, displacement, width, label =labels[0])
res2 = ax.bar(bar_x_position, forces, width, label =labels[1])
res3 = ax.bar(bar_x_position + width, num_of_elem, width, label =labels[2])

ax.set_ylabel("Przemieszczenie")
ax.set_title("Tabela")
ax.set_xticks(bar_x_position)
ax.set_xticklabels(labels)
ax.legend(["Max przemieszczenie", "Max siła normalna", "Łączna długość elementów"])

top_bar_value(res1)
top_bar_value(res2)
top_bar_value(res3)

# ax.bar_label(res1, padding=3)
# ax.bar_label(res2, padding=3)
# ax.bar_label(res3, padding=3)

fig.tight_layout()

plt.show()


# import pandas as pd
#
# df = pd.read_excel(r"D:\Programy\z.programowanie\Domes-vertices\wierzcholki.xlsx")
# df['New_column_tests'] = df['Unnamed: 13']
# writer = pd.ExcelWriter(r"D:\Programy\z.studi\ROK 6\magister\cady\asd.xlsx", engine='xlsxwriter')
# df.to_excel(writer, sheet_name='Sheet3', index=False)
# writer.save()

# from win32com.client import Dispatch
# wkbk1 = r"D:\Programy\z.studi\ROK 6\magister\cady\asd.xlsx"
# excel = Dispatch("Excel.Application")
# excel.Visible = 1
# source = excel.Workbooks.Open(wkbk1)
# excel.Range("A1:A3").Select()
# excel.Selection.Copy()
# copy = excel.Workbooks.Open(wkbk1)
# excel.Range("A6:A8").Select()
# excel.Selection.PasteSpecial(Paste=-4163)
# excel.Visible = False
# excel.Application.Quit()


import xlrd
# import os, openpyxl
# os.chdir(r"D:\Programy\z.programowanie\Domes-vertices")
# wb = openpyxl.load_workbook(r"wierzcholki.xlsx")
