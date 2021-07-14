from win32com.client import Dispatch
import os

# to be copied
path1 = r"D:\Programy\z.studi\ROK 6\magister\full_teddy_excels_plate"
# where to copy
path2 = r"D:\Programy\z.studi\ROK 6\magister\full_teddy_excels_plate_values_only"

for elem in os.listdir(path1):
    wkbk1 = os.path.join(path1, elem)
    wkbk2 = os.path.join(path2, elem)
    excel = Dispatch("Excel.Application")
    excel.Visible = 1
    source = excel.Workbooks.Open(wkbk1)
    excel.Range("A1:G800").Select()
    excel.Selection.Copy()
    copy = excel.Workbooks.Open(wkbk2)
    excel.Range("A1:G800").Select()
    excel.Selection.PasteSpecial(Paste=-4163)
    source.Application.CutCopyMode = False
    source.Save()
    excel.Quit()