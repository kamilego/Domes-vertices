import pandas as pd
import math
import numpy as np
import xlsxwriter
import pyperclip
import re
from math import sqrt

# to clear all variables
# import sys
# sys.modules[__name__].__dict__.clear()

# _____________________________TO BE SET BY USER_________________________________
dome_radius = float(10)          # metry
dome_height = dome_radius          # metry
steel = int(235)                 # MPa
s = int(1)                       # rodzaj przekroju
profile_1 = str("d 133 t 10")       # przekrój poprzeczny nr1 - mm
force = str(2513)                # siła kN
# _____________________________TO BE SET BY USER END_____________________________


def takethird(elem):
    return elem[2]


def clockwiseangle_and_distance(point):
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


def create_dictionary(dic_list, diction):
    for num, elem in enumerate(dic_list, start=1):
        diction[num] = elem


def list_of_joined_vertices(dome_list):
    ver_list = []
    for elem in dome_list:
        ver_list.append((num_vertex.findall(elem)[0].replace(" npe", "")).split(" "))
    return ver_list


def sum_of_length_count(list, diction):
    sum = 0
    for elem in list:
        l = sqrt((diction[int(elem[0])][0] - diction[int(elem[1])][0]) ** 2 +
                 (diction[int(elem[0])][1] - diction[int(elem[1])][1]) ** 2 +
                 (diction[int(elem[0])][2] - diction[int(elem[1])][2]) ** 2)
        sum += l
    return round(sum)

# załadowanie pliku excel z punktami z cada - X,Y,Z
path_1 = r"D:\Programy\z.studi\ROK 6\magister\vertices_new\vertices.xlsx"
path_2 = r"D:\Programy\z.studi\ROK 6\magister\vertices_new\vertices_lamell.xlsx"
path_3 = r"D:\Programy\z.programowanie\Domes-vertices\wierzcholki.xlsx"
path_4 = r"D:\Programy\z.studi\ROK 6\magister\to_count.xlsx"

df = pd.read_excel(path_1)
df_2 = pd.read_excel(path_2)

# stworzenie listy i transpozycja jej
mylist = [df['Position X'].tolist(), df['Position Y'].tolist(), df['Position Z'].tolist()]
mylist = list(map(list, zip(*mylist)))
mylist.sort(key=takethird)
mylist = np.array(mylist)

mylist_2 = [df_2['Position X'].tolist(), df_2['Position Y'].tolist(), df_2['Position Z'].tolist()]
mylist_2 = list(map(list, zip(*mylist_2)))
mylist_2.sort(key=takethird)
mylist_2 = np.array(mylist_2)

# założenie współrzędnych wektora
origin = [0, 0]
refvec = [0, 1]

# stworzenie list z posegregowanymi X i Y zgodnie z kierunkiem wskazówek zegara
list_a = np.array([])
list_1 = np.array(sorted(mylist[0:20], key=clockwiseangle_and_distance))
list_2 = np.array(sorted(mylist[20:40], key=clockwiseangle_and_distance))
list_3 = np.array(sorted(mylist[40:60], key=clockwiseangle_and_distance))
list_4 = np.array(sorted(mylist[60:80], key=clockwiseangle_and_distance))
list_5 = np.array(sorted(mylist[80:100], key=clockwiseangle_and_distance))
list_6 = np.array(sorted(mylist[100:120], key=clockwiseangle_and_distance))
list_7 = np.array(sorted(mylist[120:140], key=clockwiseangle_and_distance))
list_8 = np.array(sorted(mylist[140:160], key=clockwiseangle_and_distance))
list_9 = np.array(sorted(mylist[160:161]))

list2_1 = np.array(sorted(mylist_2[0:20], key=clockwiseangle_and_distance))
list2_2 = np.array(sorted(mylist_2[20:40], key=clockwiseangle_and_distance))
list2_3 = np.array(sorted(mylist_2[40:60], key=clockwiseangle_and_distance))
list2_4 = np.array(sorted(mylist_2[60:80], key=clockwiseangle_and_distance))
list2_5 = np.array(sorted(mylist_2[80:100], key=clockwiseangle_and_distance))
list2_6 = np.array(sorted(mylist_2[100:120], key=clockwiseangle_and_distance))
list2_7 = np.array(sorted(mylist_2[120:140], key=clockwiseangle_and_distance))
list2_8 = np.array(sorted(mylist_2[140:160], key=clockwiseangle_and_distance))
list2_9 = np.array(sorted(mylist_2[160:161]))


# ewentualna zmiana geometrii kopuły
r_scale = dome_radius / float(1)
h_scale = dome_height / float(1)
x2 = np.array([r_scale, r_scale, -1 * h_scale])

opus = [list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9,
        list2_1, list2_2, list2_3, list2_4, list2_5, list2_6, list2_7, list2_8, list2_9]
for n in opus:
    np.dot(n, x2)

list_1 = np.multiply(list_1, x2)
list_2 = np.multiply(list_2, x2)
list_3 = np.multiply(list_3, x2)
list_4 = np.multiply(list_4, x2)
list_5 = np.multiply(list_5, x2)
list_6 = np.multiply(list_6, x2)
list_7 = np.multiply(list_7, x2)
list_8 = np.multiply(list_8, x2)
list_9 = np.multiply(list_9, x2)
list2_1 = np.multiply(list2_1, x2)
list2_2 = np.multiply(list2_2, x2)
list2_3 = np.multiply(list2_3, x2)
list2_4 = np.multiply(list2_4, x2)
list2_5 = np.multiply(list2_5, x2)
list2_6 = np.multiply(list2_6, x2)
list2_7 = np.multiply(list2_7, x2)
list2_8 = np.multiply(list2_8, x2)
list2_9 = np.multiply(list2_9, x2)

# stworzenie dataframe do excela
dfa = pd.DataFrame(list_a)
df1 = pd.DataFrame(list_1,index=[str(i).zfill(1) for i in range(1,21)],columns=['X','Y','Z'])
df2 = pd.DataFrame(list_2,index=[str(i).zfill(1) for i in range(21,41)],columns=['X','Y','Z'])
df3 = pd.DataFrame(list_3,index=[str(i).zfill(1) for i in range(41,61)],columns=['X','Y','Z'])
df4 = pd.DataFrame(list_4,index=[str(i).zfill(1) for i in range(61,81)],columns=['X','Y','Z'])
df5 = pd.DataFrame(list_5,index=[str(i).zfill(1) for i in range(81,101)],columns=['X','Y','Z'])
df6 = pd.DataFrame(list_6,index=[str(i).zfill(1) for i in range(101,121)],columns=['X','Y','Z'])
df7 = pd.DataFrame(list_7,index=[str(i).zfill(1) for i in range(121,141)],columns=['X','Y','Z'])
df8 = pd.DataFrame(list_8,index=[str(i).zfill(1) for i in range(141,161)],columns=['X','Y','Z'])
df9 = pd.DataFrame(list_9,index=['161'],columns=['X','Y','Z'])
df11 = pd.DataFrame(list2_1,index=[str(i).zfill(1) for i in range(1,21)],columns=['X','Y','Z'])
df22 = pd.DataFrame(list2_2,index=[str(i).zfill(1) for i in range(21,41)],columns=['X','Y','Z'])
df33 = pd.DataFrame(list2_3,index=[str(i).zfill(1) for i in range(41,61)],columns=['X','Y','Z'])
df44 = pd.DataFrame(list2_4,index=[str(i).zfill(1) for i in range(61,81)],columns=['X','Y','Z'])
df55 = pd.DataFrame(list2_5,index=[str(i).zfill(1) for i in range(81,101)],columns=['X','Y','Z'])
df66 = pd.DataFrame(list2_6,index=[str(i).zfill(1) for i in range(101,121)],columns=['X','Y','Z'])
df77 = pd.DataFrame(list2_7,index=[str(i).zfill(1) for i in range(121,141)],columns=['X','Y','Z'])
df88 = pd.DataFrame(list2_8,index=[str(i).zfill(1) for i in range(141,161)],columns=['X','Y','Z'])
df99 = pd.DataFrame(list2_9,index=['161'],columns=['X','Y','Z'])

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('wierzcholki.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
dfa.to_excel(writer, sheet_name="CAŁOŚĆ")

dfy = [df1, df2, df3, df4, df5, df6, df7, df8, df9]
dfy2 = [df11, df22, df33, df44, df55, df66, df77, df88, df99]

sheet_names = []
for name in dfy:
    sheet_names.append(str(np.round(name.iloc[0]['Z'] * -1, 3)))

for num, h in enumerate(dfy):
    h.to_excel(writer, sheet_name="wysokość " + sheet_names[num])
    dfy2[num].to_excel(writer, sheet_name="wysokość " + sheet_names[num], startrow=21, startcol=0)

workbook1 = writer.book
workbook2 = writer.book
workbook3 = writer.book
workbook4 = writer.book
workbook5 = writer.book
workbook6 = writer.book
workbook7 = writer.book
workbook8 = writer.book
workbook9 = writer.book

worksheet0 = writer.sheets["CAŁOŚĆ"]
worksheet1 = writer.sheets["wysokość " + sheet_names[0]]
worksheet2 = writer.sheets["wysokość " + sheet_names[1]]
worksheet3 = writer.sheets["wysokość " + sheet_names[2]]
worksheet4 = writer.sheets["wysokość " + sheet_names[3]]
worksheet5 = writer.sheets["wysokość " + sheet_names[4]]
worksheet6 = writer.sheets["wysokość " + sheet_names[5]]
worksheet7 = writer.sheets["wysokość " + sheet_names[6]]
worksheet8 = writer.sheets["wysokość " + sheet_names[7]]
worksheet9 = writer.sheets["wysokość " + sheet_names[8]]

workbooki = [workbook1, workbook2, workbook3, workbook4, workbook5, workbook6, workbook7, workbook8, workbook9]
for g in workbooki:
    format = g.add_format({'num_format': '#,##0.0000'})


working = [worksheet1, worksheet2, worksheet3, worksheet4, worksheet5, worksheet6, worksheet7, worksheet8, worksheet9]
for k in working:
    k.set_column('B:I', None)
    k.set_column('F:F', 25)
    k.set_column('I:I', 25)

for i in working:
    for b in range(1, 42):
        if b == 21:
            continue
        i.write(b, 5, str("=A") + str(b + 1) + str("&\" \"&B") + str(b + 1) + str("&\" \"&C") + str(b + 1) + str("&\" \"&D") + str(b + 1))
        if i == worksheet1:
            i.write(b, 8, str("=") + str(b + 1000) + str("&\" npa \"&A") + str(b + 1) + str("&\" npe \"&A") + str(b + 2) + str("&\" sno ") + str(s) +str("\""))
            if b == 20 or b == 41:
                i.write(b, 8, str("=") + str(b + 1000) + str("&\" npa \"&A") + str(b - 18) + str("&\" npe \"&A") + str(b + 1) + str("&\" sno ") + str(s) +str("\""))
        if i == worksheet2:
            i.write(b, 8, str("=") + str(b + 1020) + str("&\" npa \"&A") + str(b + 1) + str("&\" npe \"&A") + str(b + 2) + str("&\" sno ") + str(s) +str("\""))
            if b == 20 or b == 41:
                i.write(b, 8, str("=") + str(b + 1020) + str("&\" npa \"&A") + str(b - 18) + str("&\" npe \"&A") + str(b + 1) + str("&\" sno ") + str(s) +str("\""))
        if i == worksheet3:
            i.write(b, 8, str("=") + str(b + 1040) + str("&\" npa \"&A") + str(b + 1) + str("&\" npe \"&A") + str(b + 2) + str("&\" sno ") + str(s) +str("\""))
            if b == 20 or b == 41:
                i.write(b, 8, str("=") + str(b + 1040) + str("&\" npa \"&A") + str(b - 18) + str("&\" npe \"&A") + str(b + 1) + str("&\" sno ") + str(s) +str("\""))
        if i == worksheet4:
            i.write(b, 8, str("=") + str(b + 1060) + str("&\" npa \"&A") + str(b + 1) + str("&\" npe \"&A") + str(b + 2) + str("&\" sno ") + str(s) +str("\""))
            if b == 20 or b == 41:
                i.write(b, 8, str("=") + str(b + 1060) + str("&\" npa \"&A") + str(b - 18) + str("&\" npe \"&A") + str(b + 1) + str("&\" sno ") + str(s) +str("\""))
        if i == worksheet5:
            i.write(b, 8, str("=") + str(b + 1080) + str("&\" npa \"&A") + str(b + 1) + str("&\" npe \"&A") + str(b + 2) + str("&\" sno ") + str(s) +str("\""))
            if b == 20 or b == 41:
                i.write(b, 8, str("=") + str(b + 1080) + str("&\" npa \"&A") + str(b - 18) + str("&\" npe \"&A") + str(b + 1) + str("&\" sno ") + str(s) +str("\""))
        if i == worksheet6:
            i.write(b, 8, str("=") + str(b + 1100) + str("&\" npa \"&A") + str(b + 1) + str("&\" npe \"&A") + str(b + 2) + str("&\" sno ") + str(s) +str("\""))
            if b == 20 or b == 41:
                i.write(b, 8, str("=") + str(b + 1100) + str("&\" npa \"&A") + str(b - 18) + str("&\" npe \"&A") + str(b + 1) + str("&\" sno ") + str(s) +str("\""))
        if i == worksheet7:
            i.write(b, 8, str("=") + str(b + 1120) + str("&\" npa \"&A") + str(b + 1) + str("&\" npe \"&A") + str(b + 2) + str("&\" sno ") + str(s) +str("\""))
            if b == 20 or b == 41:
                i.write(b, 8, str("=") + str(b + 1120) + str("&\" npa \"&A") + str(b - 18) + str("&\" npe \"&A") + str(b + 1) + str("&\" sno ") + str(s) +str("\""))
        if i == worksheet8:
            i.write(b, 8, str("=") + str(b + 1140) + str("&\" npa \"&A") + str(b + 1) + str("&\" npe \"&A") + str(b + 2) + str("&\" sno ") + str(s) +str("\""))
            if b == 20 or b == 41:
                i.write(b, 8, str("=") + str(b + 1140) + str("&\" npa \"&A") + str(b - 18) + str("&\" npe \"&A") + str(b + 1) + str("&\" sno ") + str(s) +str("\""))
        if i == worksheet9:
            break
    if i == worksheet9:
        i.write(1, 5, str("=A2&") + str("\"") + str(" ") + str("\"") + str("&B2&") + str("\"") + str(" ") + str("\"") + str("&C2&") + str("\"") + str(" ") + str("\"") + str("&D2"))
        i.write(22, 5, str("=A23&") + str("\"") + str(" ") + str("\"") + str("&B23&") + str("\"") + str(" ") + str("\"") + str("&C23&") + str("\"") + str(" ") + str("\"") + str("&D23"))
    if i == worksheet1:
        for b in range(1, 42):
            if b == 21:
                continue
            i.write(b, 5,str("=A")+ str(b + 1) + str("&\" \"&B") + str(b + 1) + str("&\" \"&C") + str(b + 1) + str("&\" \"&D") + str(b + 1) + str("&\" fix pp\""))


worksheet0.set_column('A:A', 1)
worksheet0.set_column('B:B', 70)
worksheet0.set_column('C:C', 70)
worksheet0.set_column('D:D', 70)
worksheet0.set_column('F:F', 30)
worksheet0.set_column('G:G', 30)
worksheet0.set_column('K:K', 25)
worksheet0.set_column('N:N', 25)
worksheet0.set_column('P:P', 25)
worksheet0.set_column('R:R', 25)

for t in range (2,22):
    worksheet0.write(t, 40, str("='")+str("wysokość ") + sheet_names[0] + str("'!A") + str(t))
    worksheet0.write(t, 41, str("='")+str("wysokość ") + sheet_names[1] + str("'!A") + str(t))
    worksheet0.write(t, 42, str("='")+str("wysokość ") + sheet_names[2] + str("'!A") + str(t))
    worksheet0.write(t, 43, str("='")+str("wysokość ") + sheet_names[3] + str("'!A") + str(t))
    worksheet0.write(t, 44, str("='")+str("wysokość ") + sheet_names[4] + str("'!A") + str(t))
    worksheet0.write(t, 45, str("='")+str("wysokość ") + sheet_names[5] + str("'!A") + str(t))
    worksheet0.write(t, 46, str("='")+str("wysokość ") + sheet_names[6] + str("'!A") + str(t))
    worksheet0.write(t, 47, str("='")+str("wysokość ") + sheet_names[7] + str("'!A") + str(t))
worksheet0.write(2, 48, str("='")+str("wysokość ") + sheet_names[8] + str("'!A") + str(2))


worksheet0.write(0, 1, str(" "))
worksheet0.write(0, 1, "$ Kopuła Żebrowa")
worksheet0.write(0, 2, "$ Kopuła Schwedlera")
worksheet0.write(0, 3, "$ Kopuła Lamella")
worksheet0.write(0, 5, str("$ współrzędne wierzchołków lamela"))
worksheet0.write(0, 6, str("$ współrzędne wierzchołków ż/sch"))
worksheet0.write(0, 10, str("$ połączenie poziome ż/sch"))
worksheet0.write(0, 13, str("$ połączenie pionowe ż/sch"))
worksheet0.write(0, 15, str("$ połączenie ukośne ż/sch"))


for t in range (2,162):
    worksheet0.write(t, 5, str("='") + str("wysokość ") + sheet_names[0] + str("'!F") + str(t+21))
    worksheet0.write(t, 6, str("='")+str("wysokość ") + sheet_names[0] + str("'!F") + str(t))
    worksheet0.write(t, 10, str("='")+str("wysokość ") + sheet_names[0] + str("'!I") + str(t))
    worksheet0.write(t, 13, str("=") + str(t + 10000-1) + str("&\" npa \"&AO") + str(t + 1) + str("&\" npe \"&AP") + str(t + 1) + str("&\" sno ") + str(s) +str("\""))
    worksheet0.write(t, 17, str("=") + str(t + 10400-1) + str("&\" npa \"&AP") + str(t + 1) + str("&\" npe \"&AO") + str(t + 2) + str("&\" sno ") + str(s) +str("\""))
    if t > 21:
        worksheet0.write(t, 5, str("='") + str("wysokość ") + sheet_names[1] + str("'!F") + str(t+1))
        worksheet0.write(t, 6, str("='")+str("wysokość ") + sheet_names[1] + str("'!F") + str(t-20))
        worksheet0.write(t, 10, str("='")+str("wysokość ") + sheet_names[1] + str("'!I") + str(t-20))
        worksheet0.write(t, 13,str("=") + str(t + 10000-1) + str("&\" npa \"&AP") + str(t - 19) + str("&\" npe \"&AQ") + str(t - 19) + str("&\" sno ") + str(s) +str("\""))
        worksheet0.write(t, 17, str("=") + str(t + 10400-1) + str("&\" npa \"&AP") + str(t - 19) + str("&\" npe \"&AQ") + str(t - 18) + str("&\" sno ") + str(s) +str("\""))
    if t > 41:
        worksheet0.write(t, 5, str("='") + str("wysokość ") + sheet_names[2] + str("'!F") + str(t-19))
        worksheet0.write(t, 6, str("='")+str("wysokość ") + sheet_names[2] + str("'!F") + str(t-40))
        worksheet0.write(t, 10, str("='")+str("wysokość ") + sheet_names[2] + str("'!I") + str(t-40))
        worksheet0.write(t, 13,str("=") + str(t + 10000-1) + str("&\" npa \"&AQ") + str(t - 39) + str("&\" npe \"&AR") + str(t - 39) + str("&\" sno ") + str(s) +str("\""))
        worksheet0.write(t, 17, str("=") + str(t + 10400-1) + str("&\" npa \"&AR") + str(t - 39) + str("&\" npe \"&AQ") + str(t - 38) + str("&\" sno ") + str(s) +str("\""))
    if t > 61:
        worksheet0.write(t, 5, str("='") + str("wysokość ") + sheet_names[3] + str("'!F") + str(t - 39))
        worksheet0.write(t, 6, str("='")+str("wysokość ") + sheet_names[3] + str("'!F") + str(t-60))
        worksheet0.write(t, 10, str("='")+str("wysokość ") + sheet_names[3] + str("'!I") + str(t-60))
        worksheet0.write(t, 13,str("=") + str(t + 10000-1) + str("&\" npa \"&AR") + str(t - 59) + str("&\" npe \"&AS") + str(t - 59) + str("&\" sno ") + str(s) +str("\""))
        worksheet0.write(t, 17, str("=") + str(t + 10400-1) + str("&\" npa \"&AR") + str(t - 59) + str("&\" npe \"&AS") + str(t - 58) + str("&\" sno ") + str(s) +str("\""))
    if t > 81:
        worksheet0.write(t, 5, str("='") + str("wysokość ") + sheet_names[4] + str("'!F") + str(t - 59))
        worksheet0.write(t, 6, str("='")+str("wysokość ") + sheet_names[4] + str("'!F") + str(t-80))
        worksheet0.write(t, 10, str("='")+str("wysokość ") + sheet_names[4] + str("'!I") + str(t-80))
        worksheet0.write(t, 13,str("=") + str(t + 10000-1) + str("&\" npa \"&AS") + str(t - 79) + str("&\" npe \"&AT") + str(t - 79) + str("&\" sno ") + str(s) +str("\""))
        worksheet0.write(t, 17, str("=") + str(t + 10400-1) + str("&\" npa \"&AT") + str(t - 79) + str("&\" npe \"&AS") + str(t - 78) + str("&\" sno ") + str(s) +str("\""))
    if t > 101:
        worksheet0.write(t, 5, str("='") + str("wysokość ") + sheet_names[5] + str("'!F") + str(t - 79))
        worksheet0.write(t, 6, str("='")+str("wysokość ") + sheet_names[5] + str("'!F") + str(t-100))
        worksheet0.write(t, 10, str("='")+str("wysokość ") + sheet_names[5] + str("'!I") + str(t-100))
        worksheet0.write(t, 13,str("=") + str(t + 10000-1) + str("&\" npa \"&AT") + str(t - 99) + str("&\" npe \"&AU") + str(t - 99) + str("&\" sno ") + str(s) +str("\""))
        worksheet0.write(t, 17, str("=") + str(t + 10400-1) + str("&\" npa \"&AT") + str(t - 99) + str("&\" npe \"&AU") + str(t - 98) + str("&\" sno ") + str(s) +str("\""))
    if t > 121:
        worksheet0.write(t, 5, str("='") + str("wysokość ") + sheet_names[6] + str("'!F") + str(t - 99))
        worksheet0.write(t, 6, str("='")+ str("wysokość ") + sheet_names[6] + str("'!F") + str(t-120))
        worksheet0.write(t, 10, str("='")+ str("wysokość ") + sheet_names[6] + str("'!I") + str(t-120))
        worksheet0.write(t, 13,str("=") + str(t + 10000-1) + str("&\" npa \"&AU") + str(t - 119) + str("&\" npe \"&AV") + str(t - 119) + str("&\" sno ") + str(s) +str("\""))
        worksheet0.write(t, 17, str("=") + str(t + 10400-1) + str("&\" npa \"&AV") + str(t - 119) + str("&\" npe \"&AU") + str(t - 118) + str("&\" sno ") + str(s) +str("\""))
    if t > 141:
        worksheet0.write(t, 5, str("='") + str("wysokość ") + sheet_names[7] + str("'!F") + str(t - 119))
        worksheet0.write(t, 6, str("='")+ str("wysokość ") + sheet_names[7] + str("'!F") + str(t-140))
        worksheet0.write(t, 10, str("='")+ str("wysokość ") + sheet_names[7] + str("'!I") + str(t-140))
        worksheet0.write(t, 13, str("=") + str(t + 10000 - 1) + str("&\" npa \"&AV") + str(t - 139) + str("&\" npe \"&AW3") + str("&\" sno ") + str(s) +str("\""))
    if t == 21:
        worksheet0.write(t, 17, str("=") + str(t + 10400-1) + str("&\" npa \"&AP") + str(t + 1) + str("&\" npe \"&AO") + str(t - 18) + str("&\" sno ") + str(s) +str("\""))
    if t == 41:
        worksheet0.write(t, 17, str("=") + str(t + 10400-1) + str("&\" npa \"&AP") + str(t - 19) + str("&\" npe \"&AQ") + str(t - 38) + str("&\" sno ") + str(s) +str("\""))
    if t == 61:
        worksheet0.write(t, 17,str("=") + str(t + 10400-1) + str("&\" npa \"&AR") + str(t - 39) + str("&\" npe \"&AQ") + str(t - 58) + str("&\" sno ") + str(s) + str("\""))
    if t == 81:
        worksheet0.write(t, 17,str("=") + str(t + 10400-1) + str("&\" npa \"&AR") + str(t - 59) + str("&\" npe \"&AS") + str(t - 78) + str("&\" sno ") + str(s) + str("\""))
    if t == 101:
        worksheet0.write(t, 17,str("=") + str(t + 10400-1) + str("&\" npa \"&AT") + str(t - 79) + str("&\" npe \"&AS") + str(t - 98) + str("&\" sno ") + str(s) + str("\""))
    if t == 121:
        worksheet0.write(t, 17,str("=") + str(t + 10400-1) + str("&\" npa \"&AT") + str(t - 99) + str("&\" npe \"&AU") + str(t - 118) + str("&\" sno ") + str(s) + str("\""))
    if t == 141:
        worksheet0.write(t, 17,str("=") + str(t + 10400-1) + str("&\" npa \"&AV") + str(t - 119) + str("&\" npe \"&AU") + str(t - 138) + str("&\" sno ") + str(s) + str("\""))
worksheet0.write(162, 5, str("='") + str("wysokość ") + sheet_names[8] + str("'!F") + str(23))
worksheet0.write(162, 6, str("='") + str("wysokość ") + sheet_names[8] + str("'!F") + str(2))

cells = [num for num in range(1,161,20)]

for num in range(7):
    worksheet0.write(num + 2, 15, str(num + 10200) + str(" npa ") + str(cells[num]) + str(" npe ") + str(cells[num+1]+1) + str(" sno ") + str(s))
    worksheet0.write(num + 2 + 7, 15, str(num + 7 + 10200) + str(" npa ") + str(cells[num]+2) + str(" npe ") + str(cells[num+1]+3) + str(" sno ") + str(s))
    worksheet0.write(num + 2 + 14, 15, str(num + 14 + 10200) + str(" npa ") + str(cells[num]+4) + str(" npe ") + str(cells[num+1]+5) + str(" sno ") + str(s))
    worksheet0.write(num + 2 + 21, 15, str(num + 21 + 10200) + str(" npa ") + str(cells[num]+6) + str(" npe ") + str(cells[num+1]+7) + str(" sno ") + str(s))
    worksheet0.write(num + 2 + 28, 15, str(num + 28 + 10200) + str(" npa ") + str(cells[num]+8) + str(" npe ") + str(cells[num+1]+9) + str(" sno ") + str(s))
    worksheet0.write(num + 2 + 35, 15, str(num + 35 + 10200) + str(" npa ") + str(cells[num]+10) + str(" npe ") + str(cells[num+1]+11) + str(" sno ") + str(s))
    worksheet0.write(num + 2 + 42, 15, str(num + 42 + 10200) + str(" npa ") + str(cells[num]+12) + str(" npe ") + str(cells[num+1]+13) + str(" sno ") + str(s))
    worksheet0.write(num + 2 + 49, 15, str(num + 49 + 10200) + str(" npa ") + str(cells[num]+14) + str(" npe ") + str(cells[num+1]+15) + str(" sno ") + str(s))
    worksheet0.write(num + 2 + 56, 15, str(num + 56 + 10200) + str(" npa ") + str(cells[num]+16) + str(" npe ") + str(cells[num+1]+17) + str(" sno ") + str(s))
    worksheet0.write(num + 2 + 63, 15, str(num + 63 + 10200) + str(" npa ") + str(cells[num]+18) + str(" npe ") + str(cells[num+1]+19) + str(" sno ") + str(s))
    worksheet0.write(num + 72, 15, str(num + 10300) + str(" npa ") + str(cells[num]+2) + str(" npe ") + str(cells[num+1]+1) + str(" sno ") + str(s))
    worksheet0.write(num + 72 + 7, 15, str(num + 7 + 10300) + str(" npa ") + str(cells[num]+4) + str(" npe ") + str(cells[num+1]+3) + str(" sno ") + str(s))
    worksheet0.write(num + 72 + 14, 15, str(num + 14 + 10300) + str(" npa ") + str(cells[num]+6) + str(" npe ") + str(cells[num+1]+5) + str(" sno ") + str(s))
    worksheet0.write(num + 72 + 21, 15, str(num + 21 + 10300) + str(" npa ") + str(cells[num]+8) + str(" npe ") + str(cells[num+1]+7) + str(" sno ") + str(s))
    worksheet0.write(num + 72 + 28, 15, str(num + 28 + 10300) + str(" npa ") + str(cells[num]+10) + str(" npe ") + str(cells[num+1]+9) + str(" sno ") + str(s))
    worksheet0.write(num + 72 + 35, 15, str(num + 35 + 10300) + str(" npa ") + str(cells[num]+12) + str(" npe ") + str(cells[num+1]+11) + str(" sno ") + str(s))
    worksheet0.write(num + 72 + 42, 15, str(num + 42 + 10300) + str(" npa ") + str(cells[num]+14) + str(" npe ") + str(cells[num+1]+13) + str(" sno ") + str(s))
    worksheet0.write(num + 72 + 49, 15, str(num + 49 + 10300) + str(" npa ") + str(cells[num]+16) + str(" npe ") + str(cells[num+1]+15) + str(" sno ") + str(s))
    worksheet0.write(num + 72 + 56, 15, str(num + 56 + 10300) + str(" npa ") + str(cells[num]+18) + str(" npe ") + str(cells[num+1]+17) + str(" sno ") + str(s))
    worksheet0.write(num + 72 + 63, 15, str(num + 63 + 10300) + str(" npa ") + str(cells[num]) + str(" npe ") + str(cells[num+1]+19) + str(" sno ") + str(s))


for t in range(1, 4):
    worksheet0.write(2, t, "+prog aqua urs:1")
    worksheet0.write(3, t, "head przekroje+materialy")
    worksheet0.write(4, t, "echo full")
    worksheet0.write(6, t, "$ norma")
    worksheet0.write(7, t, "norm dc en ndc 1993-2005 coun 00 unit 5  $ unit sets AQUA-pomoc strona 3-2")
    worksheet0.write(9, t, "$ materialy")
    worksheet0.write(10, t, "stee no 1 type s clas " + str(steel) + " $ stal")
    worksheet0.write(12, t, "$ przekroj poprzeczny")
    worksheet0.write(14, t, "scit no 1  " + profile_1 + " mno 1")
    worksheet0.write(17, t, "end")
    worksheet0.write(19, t, "+prog sofimshc urs:2")
    worksheet0.write(20, t, "head geometria")
    worksheet0.write(21, t, "syst 3d")
    worksheet0.write(22, t, "echo full")
    worksheet0.write(24, t, "ctrl mesh 0.5; ctrl hmin 1.0 $ PARAMETRY GENERATORA SIATKI ES")
    worksheet0.write(26, t, "$ PUNKTY definicja")
    worksheet0.write(27, t, "=\"spt no \""+str("&G3"))
    if t == 3:
        worksheet0.write(27, t, "=\"spt no \"" + str("&F3"))
    for z in range(28, 28+160):
        worksheet0.write(z, t, str("=G")+str(z-24))
        if t == 3:
            worksheet0.write(z, t, str("=F") + str(z - 24))
    worksheet0.write(199, t, "$ definicja konstrukcji")
    worksheet0.write(200, t, "=\"sln no \""+str("&K23"))
    for z in range(201, 340):
        worksheet0.write(z, t, str("=K")+str(z-177))
    for z in range(340, 340+160):
        worksheet0.write(z, t, str("=N")+str(z-337))
    if t == 2:
        for z in range(340+160, 340+160+140):
            worksheet0.write(z, t, str("=P") + str(z - 497))
    if t == 3:
        for z in range(340+160, 340+160+140):
            worksheet0.write(z, t, str("=R") + str(z - 497))
    worksheet0.write(700, t, str("end"))
    worksheet0.write(701, t, "+prog sofiload urs:4")
    worksheet0.write(702, t, "head obciazenia")
    worksheet0.write(703, t, "lc 1 dlz 1 titl obc_cw")
    worksheet0.write(704, t, "lc 2 titl obc_skupione")
    worksheet0.write(705, t, "node no 161 type pzz p1 " + str(force))
    worksheet0.write(706, t, "end")
    worksheet0.write(708, t, "+prog ase urs:5")
    worksheet0.write(709, t, "head obliczenia")
    worksheet0.write(710, t, "lc 1,2")
    worksheet0.write(711, t, "end")
    worksheet0.write(713, t, "+prog ase urs:10")
    worksheet0.write(714, t, "head kombinacja")
    worksheet0.write(715, t, "lc 4 dlz 1.35 titl suma")
    worksheet0.write(716, t, "lcc 2 fact 1.5")
    worksheet0.write(717, t, "end")


# zapisz.
writer.save()


#vertices = pd.read_excel(r"D:\Programy\z.programowanie\Domes-vertices\wierzcholki.xlsx")
#pyperclip.copy(vertices["$ Kopuła Żebrowa"].to_string(index=False))


all_lists = np.concatenate((list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9)).tolist()
all_lists_2 = np.concatenate((list2_1, list2_2, list2_3, list2_4, list2_5, list2_6, list2_7, list2_8, list2_9)).tolist()

dic_vertices = {}
dic_vertices_lamell = {}

create_dictionary(all_lists, dic_vertices)
create_dictionary(all_lists_2, dic_vertices_lamell)

read_excel = pd.read_excel(r"D:\Programy\z.studi\ROK 6\magister\to_count.xlsx", index_col=0)

dome_1 = read_excel.iloc[:, 0].tolist()[199:499]
dome_2 = read_excel.iloc[:, 1].tolist()[199:639]
dome_3 = read_excel.iloc[:, 2].tolist()[199:639]

num_vertex = re.compile(r'\d npe \d|\d npe \d\d|\d\d npe \d|\d\d npe \d\d|\d\d npe \d\d\d|\d\d\d npe \d\d|\d\d\d npe \d\d\d')

dome_1_list = list_of_joined_vertices(dome_1)
dome_2_list = list_of_joined_vertices(dome_2)
dome_3_list = list_of_joined_vertices(dome_3)

dome_1_length = sum_of_length_count(dome_1_list, dic_vertices)
dome_2_length = sum_of_length_count(dome_2_list, dic_vertices)
dome_3_length = sum_of_length_count(dome_3_list, dic_vertices_lamell)
