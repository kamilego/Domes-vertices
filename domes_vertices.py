import pandas as pd
import math
import numpy as np
#import xlrd

# to clear all variables
# import sys
# sys.modules[__name__].__dict__.clear()

#_____________________________DANE DO WPROWADZENIA_____________________________
promien = float(1)              #metry
strzalka = float(1)             #metry
stal = int(235)                 #MPa
s = int(2)                      #rodzaj przekroju
przekroj1 = str("HEB 600")      #przekrój poprzeczny nr1 - mm
przekroj2 = str("d 200 t 20")   #przekrój poprzeczny nr2 - mm
sila = str(1000)                #siła kN
#_____________________________DANE DO WPROWADZENIA_____________________________


def takeThird(elem):
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
    dotprod  = normalized[0]*refvec[0] + normalized[1]*refvec[1]     # x1*x2 + y1*y2
    diffprod = refvec[1]*normalized[0] - refvec[0]*normalized[1]     # x1*y2 - y1*x2
    angle = math.atan2(diffprod, dotprod)
    # Negative angles represent counter-clockwise angles so we need to subtract them
    # from 2*pi (360 degrees)
    if angle < 0:
        return 2*math.pi+angle, lenvector
    # I return first the angle because that's the primary sorting criterium
    # but if two vectors have the same angle then the shorter distance should come first.
    return angle, lenvector

# załadowanie pliku excel z punktami z cada - X,Y,Z
df = pd.read_excel (r"D:\Programy\z.studi\ROK 5\magister\wierzchołki.xlsx")
df_2 = pd.read_excel (r"D:\Programy\z.studi\ROK 5\magister\kopuła_wierzchołk2.xls.xlsx")

# stworzenie listy i transpozycja jej
mylist = [df['Position X'].tolist(),df['Position Y'].tolist(),df['Position Z'].tolist()]
mylist = list(map(list, zip(*mylist)))
mylist.sort(key=takeThird)
mylist = np.array(mylist)

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

# ewentualna zmiana geometrii kopuły
r_scale= promien/float(1)
h_scale = strzalka/float(1)
x2 = np.array([r_scale, r_scale, -1 * h_scale])

opus = [list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9]
for n in opus:
    np.dot(n,x2)
list_1 = np.multiply(list_1, x2)
list_2 = np.multiply(list_2, x2)
list_3 = np.multiply(list_3, x2)
list_4 = np.multiply(list_4, x2)
list_5 = np.multiply(list_5, x2)
list_6 = np.multiply(list_6, x2)
list_7 = np.multiply(list_7, x2)
list_8 = np.multiply(list_8, x2)
list_9 = np.multiply(list_9, x2)

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

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('wierzcholki.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
dfa.to_excel(writer, sheet_name="CAŁOŚĆ")

dfy = [df1, df2, df3, df4, df5, df6, df7, df8, df9]
for h in dfy:
    h.to_excel(writer, sheet_name="wysokość " + str(h.iloc[0]['Z'] * -1))

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
worksheet1 = writer.sheets["wysokość " +str(df1.iloc[0]['Z']*-1)]
worksheet2 = writer.sheets["wysokość " +str(df2.iloc[0]['Z']*-1)]
worksheet3 = writer.sheets["wysokość " +str(df3.iloc[0]['Z']*-1)]
worksheet4 = writer.sheets["wysokość " +str(df4.iloc[0]['Z']*-1)]
worksheet5 = writer.sheets["wysokość " +str(df5.iloc[0]['Z']*-1)]
worksheet6 = writer.sheets["wysokość " +str(df6.iloc[0]['Z']*-1)]
worksheet7 = writer.sheets["wysokość " +str(df7.iloc[0]['Z']*-1)]
worksheet8 = writer.sheets["wysokość " +str(df8.iloc[0]['Z']*-1)]
worksheet9 = writer.sheets["wysokość " +str(df9.iloc[0]['Z']*-1)]

workbooki = [workbook1,workbook2,workbook3,workbook4,workbook5,workbook6,workbook7,workbook8,workbook9]
for g in workbooki:
    format = g.add_format({'num_format': '#,##0.0000'})


working = [worksheet1,worksheet2,worksheet3,worksheet4,worksheet5,worksheet6,worksheet7,worksheet8,worksheet9]
for k in working:
    k.set_column('B:I', None)
    k.set_column('F:F', 25)
    k.set_column('I:I', 25)

for i in working:
    for b in range(1, 21):
        i.write(b, 5, str("=A") + str(b + 1) + str("&\" \"&B") + str(b + 1) + str("&\" \"&C") + str(b + 1) + str("&\" \"&D") + str(b + 1))
        if i == worksheet1:
            i.write(b, 8, str("=") + str(b + 1000) + str("&\" npa \"&A") + str(b + 1) + str("&\" npe \"&A") + str(b + 2) + str("&\" sno ") + str(s) +str("\""))
        if b == 20:
            i.write(b, 8, str("=") + str(b + 1000) + str("&\" npa \"&A") + str(b - 18) + str("&\" npe \"&A") + str(b + 1) + str("&\" sno ") + str(s) +str("\""))
        if i == worksheet2:
            i.write(b, 8, str("=") + str(b + 1020) + str("&\" npa \"&A") + str(b + 1) + str("&\" npe \"&A") + str(b + 2) + str("&\" sno ") + str(s) +str("\""))
            if b == 20:
                i.write(b, 8, str("=") + str(b + 1020) + str("&\" npa \"&A") + str(b - 18) + str("&\" npe \"&A") + str(b + 1) + str("&\" sno ") + str(s) +str("\""))
        if i == worksheet3:
            i.write(b, 8, str("=") + str(b + 1040) + str("&\" npa \"&A") + str(b + 1) + str("&\" npe \"&A") + str(b + 2) + str("&\" sno ") + str(s) +str("\""))
            if b == 20:
                i.write(b, 8, str("=") + str(b + 1040) + str("&\" npa \"&A") + str(b - 18) + str("&\" npe \"&A") + str(b + 1) + str("&\" sno ") + str(s) +str("\""))
        if i == worksheet4:
            i.write(b, 8, str("=") + str(b + 1060) + str("&\" npa \"&A") + str(b + 1) + str("&\" npe \"&A") + str(b + 2) + str("&\" sno ") + str(s) +str("\""))
            if b == 20:
                i.write(b, 8, str("=") + str(b + 1060) + str("&\" npa \"&A") + str(b - 18) + str("&\" npe \"&A") + str(b + 1) + str("&\" sno ") + str(s) +str("\""))
        if i == worksheet5:
            i.write(b, 8, str("=") + str(b + 1080) + str("&\" npa \"&A") + str(b + 1) + str("&\" npe \"&A") + str(b + 2) + str("&\" sno ") + str(s) +str("\""))
            if b == 20:
                i.write(b, 8, str("=") + str(b + 1080) + str("&\" npa \"&A") + str(b - 18) + str("&\" npe \"&A") + str(b + 1) + str("&\" sno ") + str(s) +str("\""))
        if i == worksheet6:
            i.write(b, 8, str("=") + str(b + 1100) + str("&\" npa \"&A") + str(b + 1) + str("&\" npe \"&A") + str(b + 2) + str("&\" sno ") + str(s) +str("\""))
            if b == 20:
                i.write(b, 8, str("=") + str(b + 1100) + str("&\" npa \"&A") + str(b - 18) + str("&\" npe \"&A") + str(b + 1) + str("&\" sno ") + str(s) +str("\""))
        if i == worksheet7:
            i.write(b, 8, str("=") + str(b + 1120) + str("&\" npa \"&A") + str(b + 1) + str("&\" npe \"&A") + str(b + 2) + str("&\" sno ") + str(s) +str("\""))
            if b == 20:
                i.write(b, 8, str("=") + str(b + 1120) + str("&\" npa \"&A") + str(b - 18) + str("&\" npe \"&A") + str(b + 1) + str("&\" sno ") + str(s) +str("\""))
        if i == worksheet8:
            i.write(b, 8, str("=") + str(b + 1140) + str("&\" npa \"&A") + str(b + 1) + str("&\" npe \"&A") + str(b + 2) + str("&\" sno ") + str(s) +str("\""))
            if b == 20:
                i.write(b, 8, str("=") + str(b + 1140) + str("&\" npa \"&A") + str(b - 18) + str("&\" npe \"&A") + str(b + 1) + str("&\" sno ") + str(s) +str("\""))
        if i == worksheet9:
            break
    if i ==  worksheet9:
        i.write(1, 5, str("=A2&") + str("\"") + str(" ") + str("\"") + str("&B2&") + str("\"") + str(" ") + str("\"") + str("&C2&") + str("\"") + str(" ") + str("\"") + str("&D2"))
    if i == worksheet1:
        for b in range(1, 21):
            i.write(b, 5,str("=A")+ str(b + 1) + str("&\" \"&B") + str(b + 1) + str("&\" \"&C") + str(b + 1) + str("&\" \"&D") + str(b + 1) + str("&\" fix ppmm\""))


worksheet0.set_column('D:D', 70)
worksheet0.set_column('E:E', 70)
worksheet0.set_column('G:G', 25)
worksheet0.set_column('K:K', 25)
worksheet0.set_column('N:N', 25)
worksheet0.set_column('P:P', 25)

for t in range (2,22):
    worksheet0.write(t, 40, str("='")+str("wysokość ") +str(df1.iloc[0]['Z']*-1)+ str("'!A") + str(t))
    worksheet0.write(t, 41, str("='")+str("wysokość ") +str(df2.iloc[0]['Z']*-1)+ str("'!A") + str(t))
    worksheet0.write(t, 42, str("='")+str("wysokość ") +str(df3.iloc[0]['Z']*-1)+ str("'!A") + str(t))
    worksheet0.write(t, 43, str("='")+str("wysokość ") +str(df4.iloc[0]['Z']*-1)+ str("'!A") + str(t))
    worksheet0.write(t, 44, str("='")+str("wysokość ") +str(df5.iloc[0]['Z']*-1)+ str("'!A") + str(t))
    worksheet0.write(t, 45, str("='")+str("wysokość ") +str(df6.iloc[0]['Z']*-1)+ str("'!A") + str(t))
    worksheet0.write(t, 46, str("='")+str("wysokość ") +str(df7.iloc[0]['Z']*-1)+ str("'!A") + str(t))
    worksheet0.write(t, 47, str("='")+str("wysokość ") +str(df8.iloc[0]['Z']*-1)+ str("'!A") + str(t))
worksheet0.write(2, 48, str("='")+str("wysokość ") +str(df9.iloc[0]['Z']*-1)+ str("'!A") + str(2))

worksheet0.write(0, 3, str("Kopuła Żebrowa"))
worksheet0.write(0, 4, str("Kopuła Schwedlera"))
worksheet0.write(0, 6, str("współrzędne wierzchołków"))
worksheet0.write(0, 10, str("połączenie poziome"))
worksheet0.write(0, 13, str("połączenie pionowe"))
worksheet0.write(0, 15, str("połączenie ukośne"))


for t in range (2,162):
    worksheet0.write(t, 6, str("='")+str("wysokość ") +str(df1.iloc[0]['Z']*-1)+ str("'!F") + str(t))
    worksheet0.write(t, 10, str("='")+str("wysokość ") +str(df1.iloc[0]['Z']*-1)+ str("'!I") + str(t))
    worksheet0.write(t, 13, str("=") + str(t + 10000-1) + str("&\" npa \"&AO") + str(t + 1) + str("&\" npe \"&AP") + str(t + 1) + str("&\" sno ") + str(s) +str("\""))
    worksheet0.write(t, 15, str("=") + str(t + 10200-1) + str("&\" npa \"&AO") + str(t + 1) + str("&\" npe \"&AP") + str(t + 2) + str("&\" sno ") + str(s) +str("\""))
    if t > 21:
        worksheet0.write(t, 6, str("='")+str("wysokość ") +str(df2.iloc[0]['Z']*-1)+ str("'!F") + str(t-20))
        worksheet0.write(t, 10, str("='")+str("wysokość ") +str(df2.iloc[0]['Z']*-1)+ str("'!I") + str(t-20))
        worksheet0.write(t, 13,str("=") + str(t + 10000-1) + str("&\" npa \"&AP") + str(t - 19) + str("&\" npe \"&AQ") + str(t - 19) + str("&\" sno ") + str(s) +str("\""))
        worksheet0.write(t, 15, str("=") + str(t + 10200-1) + str("&\" npa \"&AP") + str(t - 19) + str("&\" npe \"&AQ") + str(t - 18) + str("&\" sno ") + str(s) +str("\""))
    if t > 41:
        worksheet0.write(t, 6, str("='")+str("wysokość ") +str(df3.iloc[0]['Z']*-1)+ str("'!F") + str(t-40))
        worksheet0.write(t, 10, str("='")+str("wysokość ") +str(df3.iloc[0]['Z']*-1)+ str("'!I") + str(t-40))
        worksheet0.write(t, 13,str("=") + str(t + 10000-1) + str("&\" npa \"&AQ") + str(t - 39) + str("&\" npe \"&AR") + str(t - 39) + str("&\" sno ") + str(s) +str("\""))
        worksheet0.write(t, 15, str("=") + str(t + 10200-1) + str("&\" npa \"&AQ") + str(t - 39) + str("&\" npe \"&AR") + str(t - 38) + str("&\" sno ") + str(s) +str("\""))
    if t > 61:
        worksheet0.write(t, 6, str("='")+str("wysokość ") +str(df4.iloc[0]['Z']*-1)+ str("'!F") + str(t-60))
        worksheet0.write(t, 10, str("='")+str("wysokość ") +str(df4.iloc[0]['Z']*-1)+ str("'!I") + str(t-60))
        worksheet0.write(t, 13,str("=") + str(t + 10000-1) + str("&\" npa \"&AR") + str(t - 59) + str("&\" npe \"&AS") + str(t - 59) + str("&\" sno ") + str(s) +str("\""))
        worksheet0.write(t, 15, str("=") + str(t + 10200-1) + str("&\" npa \"&AR") + str(t - 59) + str("&\" npe \"&AS") + str(t - 58) + str("&\" sno ") + str(s) +str("\""))
    if t > 81:
        worksheet0.write(t, 6, str("='")+str("wysokość ") +str(df5.iloc[0]['Z']*-1)+ str("'!F") + str(t-80))
        worksheet0.write(t, 10, str("='")+str("wysokość ") +str(df5.iloc[0]['Z']*-1)+ str("'!I") + str(t-80))
        worksheet0.write(t, 13,str("=") + str(t + 10000-1) + str("&\" npa \"&AS") + str(t - 79) + str("&\" npe \"&AT") + str(t - 79) + str("&\" sno ") + str(s) +str("\""))
        worksheet0.write(t, 15, str("=") + str(t + 10200-1) + str("&\" npa \"&AS") + str(t - 79) + str("&\" npe \"&AT") + str(t - 78) + str("&\" sno ") + str(s) +str("\""))
    if t > 101:
        worksheet0.write(t, 6, str("='")+str("wysokość ") +str(df6.iloc[0]['Z']*-1)+ str("'!F") + str(t-100))
        worksheet0.write(t, 10, str("='")+str("wysokość ") +str(df6.iloc[0]['Z']*-1)+ str("'!I") + str(t-100))
        worksheet0.write(t, 13,str("=") + str(t + 10000-1) + str("&\" npa \"&AT") + str(t - 99) + str("&\" npe \"&AU") + str(t - 99) + str("&\" sno ") + str(s) +str("\""))
        worksheet0.write(t, 15, str("=") + str(t + 10200-1) + str("&\" npa \"&AT") + str(t - 99) + str("&\" npe \"&AU") + str(t - 98) + str("&\" sno ") + str(s) +str("\""))
    if t > 121:
        worksheet0.write(t, 6, str("='")+str("wysokość ") +str(df7.iloc[0]['Z']*-1)+ str("'!F") + str(t-120))
        worksheet0.write(t, 10, str("='")+str("wysokość ") +str(df7.iloc[0]['Z']*-1)+ str("'!I") + str(t-120))
        worksheet0.write(t, 13,str("=") + str(t + 10000-1) + str("&\" npa \"&AU") + str(t - 119) + str("&\" npe \"&AV") + str(t - 119) + str("&\" sno ") + str(s) +str("\""))
        worksheet0.write(t, 15, str("=") + str(t + 10200-1) + str("&\" npa \"&AU") + str(t - 119) + str("&\" npe \"&AV") + str(t - 118) + str("&\" sno ") + str(s) +str("\""))
    if t > 141:
        worksheet0.write(t, 6, str("='")+str("wysokość ") +str(df8.iloc[0]['Z']*-1)+ str("'!F") + str(t-140))
        worksheet0.write(t, 10, str("='")+str("wysokość ") +str(df8.iloc[0]['Z']*-1)+ str("'!I") + str(t-140))
        worksheet0.write(t, 13, str("=") + str(t + 10000 - 1) + str("&\" npa \"&AV") + str(t - 139) + str("&\" npe \"&AW3") + str("&\" sno ") + str(s) +str("\""))
    if t == 21:
        worksheet0.write(t, 15,str("=") + str(t + 10200 - 1) + str("&\" npa \"&AO") + str(t + 1) + str("&\" npe \"&AP") + str(t - 18) + str("&\" sno ") + str(s) + str("\""))
    if t == 41:
        worksheet0.write(t, 15,str("=") + str(t + 10200 - 1) + str("&\" npa \"&AP") + str(t - 19) + str("&\" npe \"&AQ") + str(t - 38) + str("&\" sno ") + str(s) + str("\""))
    if t == 61:
        worksheet0.write(t, 15,str("=") + str(t + 10200 - 1) + str("&\" npa \"&AQ") + str(t - 39) + str("&\" npe \"&AR") + str(t - 58) + str("&\" sno ") + str(s) + str("\""))
    if t == 81:
        worksheet0.write(t, 15,str("=") + str(t + 10200 - 1) + str("&\" npa \"&AR") + str(t - 59) + str("&\" npe \"&AS") + str(t - 78) + str("&\" sno ") + str(s) + str("\""))
    if t == 101:
        worksheet0.write(t, 15,str("=") + str(t + 10200 - 1) + str("&\" npa \"&AS") + str(t - 79) + str("&\" npe \"&AT") + str(t - 98) + str("&\" sno ") + str(s) + str("\""))
    if t == 121:
        worksheet0.write(t, 15,str("=") + str(t + 10200 - 1) + str("&\" npa \"&AT") + str(t - 99) + str("&\" npe \"&AU") + str(t - 118) + str("&\" sno ") + str(s) + str("\""))
    if t == 141:
        worksheet0.write(t, 15,str("=") + str(t + 10200 - 1) + str("&\" npa \"&AU") + str(t - 119) + str("&\" npe \"&AV") + str(t - 138) + str("&\" sno ") + str(s) + str("\""))
worksheet0.write(162, 6, str("='")+str("wysokość ") +str(df9.iloc[0]['Z']*-1)+ str("'!F") + str(2))

for t in range (3,5):
    worksheet0.write(1, t, "+prog aqua urs:1")
    worksheet0.write(2, t, "head przekroje+materialy")
    worksheet0.write(3, t, "echo full")
    worksheet0.write(5, t, "$ norma")
    worksheet0.write(6, t, "norm dc en ndc 1993-2005 coun 00 unit 5  $ unit sets AQUA-pomoc strona 3-2")
    worksheet0.write(8, t, "$ materialy")
    worksheet0.write(9, t, "stee no 1 type s clas "+ str(stal) + " $ stal")
    worksheet0.write(11, t, "$ przekroj poprzeczny")
    worksheet0.write(13, t, "prof no 1 type " + przekroj1 +" mno 1")
    worksheet0.write(15, t, "scit no 2 " + przekroj2 +" mno 1")
    worksheet0.write(17, t, "end")
    worksheet0.write(19, t, "+prog sofimshc urs:2")
    worksheet0.write(20, t, "head geometria")
    worksheet0.write(21, t, "syst 3d")
    worksheet0.write(22, t, "echo full")
    worksheet0.write(24, t, "ctrl mesh 1; ctrl hmin 1 $ PARAMETRY GENERATORA SIATKI ES")
    worksheet0.write(26, t, "$ PUNKTY definicja")
    worksheet0.write(27, t, "=\"spt no \""+str("&G3"))
    for z in range (28, 28+160):
        worksheet0.write(z, t, str("=G")+str(z-24))
    worksheet0.write(199, t, "$ definicja konstrukcji")
    worksheet0.write(200, t, "=\"sln no \""+str("&K3"))
    for z in range (201, 360):
        worksheet0.write(z, t, str("=K")+str(z-197))
    for z in range (360, 360+160):
        worksheet0.write(z, t, str("=N")+str(z-357))
    if t ==4:
        for z in range (360+160,360+160+140):
            worksheet0.write(z, t, str("=P") + str(z - 517))


    worksheet0.write(700, t, str("end"))
    worksheet0.write(701, t, "+prog sofiload urs:4")
    worksheet0.write(702, t, "head obciazenia")
    worksheet0.write(703, t, "lc 1 dlz 1 titl obc_cw")
    worksheet0.write(704, t, "lc 2 titl obc_skupione")
    worksheet0.write(705, t, "node no 161 type pzz p1 "+str(sila))
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