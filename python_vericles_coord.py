import os
import numpy as np
import math
from math import sqrt
import re


def quad_lamell():
    def all_names(param, sum,  a4, a5, a1=0, a2=1, a3=19):
        lista = []
        for num in range(param-19, param+21):
            if num < param+1:
                if num != param:
                    lista.append(f"{sum} n1 {num+a1} n2 {num+a2} n3 {num+a4} mno 1 posi cent t 1")
                    sum += 1
                else:
                    lista.append(f"{sum} n1 {num+a1} n2 {num-a3} n3 {num+a5} mno 1 posi cent t 1")
                    sum += 1
            else:
                if num != param+1:
                    lista.append(f"{sum} n1 {num-a4} n2 {num+a1} n3 {num-a2} mno 1 posi cent t 1")
                    sum += 1
                else:
                    lista.append(f"{sum} n1 {num-a5} n2 {num+a1} n3 {num+a3} mno 1 posi cent t 1") 
                    sum += 1
        return lista

    def lnames(param):
        lista = []
        for num in range(param+1, param+20):
            lista.append(f"{140+num} n1 {num} n2 {1+num} n3 161 mno 1 posi cent t 1")
        if num < 160:
            lista.append(f"{141+num} n1 {num+1} n2 {num-18} n3 161 mno 1 posi cent t 1")
        return lista

    f_list = []
    test1 = 1
    for num in range(20, 140, 40):
        # fnames
        f_list.extend(all_names(num, test1, 20, 20))
        # snames
        f_list.extend(all_names(num+20, test1+40, 21, 1))
        test1 += 80
    # fnames
    f_list.extend(all_names(140, 341, 20, 20))
    f_list.extend(lnames(140))
    add_teddy_elem(f_list, "quad no")
    return f_list

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def final_join(summary):
    small_list = []
    for num in range(141,160):
        small_list.append(f"{summary} n1 {num} n2 {num+1} n3 161 mno 1 posi cent t 1")
        summary += 1
        if num == 159:
            small_list.append(f"{summary} n1 160 n2 141 n3 161 mno 1 posi cent t 1")
    return small_list


def quad_schwedler():
    def final_vert_names(param, sum, a1, a2, a3, a4):
        lista = []
        for num in range(param, param+121, 20):
            lista.append(f"{sum} n1 {num} n2 {num+a1} n3 {num+a2} mno 1 posi cent t 1")
            sum += 1
            lista.append(f"{sum} n1 {num} n2 {num+a3} n3 {num+a4} mno 1 posi cent t 1")
            sum += 1
        return lista

    names_list = []
    summary = 1
    for num in range(2,19,2):
        names_list.extend(final_vert_names(num, summary, 19, -1, 20, 19))
        summary += 14
        names_list.extend(final_vert_names(num, summary, 21, 20, 1, 21))
        summary += 14

    names_list.extend(final_vert_names(20, summary, 1, 20, -19, 1))
    summary += 14
    names_list.extend(final_vert_names(20, summary, 20, 19, 19, -1))
    summary += 14

    names_list.extend(final_join(summary))
    add_teddy_elem(names_list, "quad no")
    return names_list

def quad_zebrowa():
    def zebrowa_poles(param, sum):
        lista = []
        for num in range(param, 141):
            if not num % 20 ==0:
                lista.append(f"{sum} n1 {num} n2 {num+1} n3 {num+21} n4 {num+20} mno 1 posi cent t 1")
                sum +=1
            else:
                lista.append(f"{sum} n1 {num} n2 {num-19} n3 {num+1} n4 {num+20} mno 1 posi cent t 1")
                sum +=1
        return [lista, sum]
    
    f_list = zebrowa_poles(1, 1)
    f_list[0].extend(final_join(zebrowa_poles(1, 1)[1]))
    add_teddy_elem(f_list[0], "quad no")
    return f_list[0]

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def dome_join(param, count, impr, step, plus, sp1, sp2, sp3, sp4):
    lista = []
    for num in range(param, param+impr, step):
        if num < param+plus:
            lista.append(f"{count} na {num} ne {num+sp1} ncs 1")
            count += 1
        else:
            lista.append(f"{count} na {num} ne {(num-sp2)*sp3+161*sp4} ncs 1")
    return lista

def add_teddy_elem(dome_list, elem_type):
    for i in range(len(dome_list)):
        if i == 0:
            dome_list[0] = f"{elem_type} {dome_list[0]}"

def domes_sticks(param, count, add, step, var, sp1, sp2):
    lista = []
    for num in range(param, param+add, step):
        if num < param+var:
            lista.append(f"{count} na {num} ne {num+20+sp1} ncs 1")
            count += 1
            lista.append(f"{count} na {num+20+sp1} ne {num+step} ncs 1")
            count += 1
        else:
            lista.append(f"{count} na {num} ne {num+sp2} ncs 1")
            count += 1
            lista.append(f"{count} na {num+sp2} ne {num-add+1} ncs 1")
            count += 1
    return lista


def beam_lamell():
    check_list = []
    for num, param in enumerate([num for num in range(1, 142, 20)], start=1):
        if param < 141:
            if num % 2 == 0:
                check_list.extend(domes_sticks(param, param*2 - 1, add=20, step=1, var=19, sp1=1, sp2=1))
            else:
                check_list.extend(domes_sticks(param, param*2 - 1, add=20, step=1, var=19, sp1=0, sp2=20))
        else:
            for num in range(param, param+20):
                check_list.append(f"{num+140} na {num} ne 161 ncs 1")
    for num in range(21, 142, 20):
        check_list.extend(dome_join(num, count=280+num, impr=20, step=1, plus=19, sp1=1, sp2=19, sp3=1, sp4=0))
    add_teddy_elem(check_list, "beam no")
    return check_list


def beam_schwedler():
    lista = []
    for num in range(1, 21):
        lista.extend(dome_join(num, count=-7+num*8, impr=141, step=20, plus=121, sp1=20, sp2=161, sp3=0, sp4=1))
    for num in range(21, 142, 20):
        lista.extend(dome_join(num, count=140+num, impr=20, step=1, plus=19, sp1=1, sp2=19, sp3=1, sp4=0))
    for num, param in enumerate([num for num in range(2, 141, 20)], start=1):
        lista.extend(domes_sticks(param, 299+param, add=19, step=2, var=17, sp1=1, sp2=1))
    add_teddy_elem(lista, "beam no")
    return lista

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# end quads functions

def change_dome_list_to_teddy(dome_list):
    for i in range(len(dome_list)):
        dome_list[i] = str(dome_list[i]).replace("[", "").replace("]","")
        dome_list[i] = f"{i+1} {dome_list[i]}"
        if i == 0:
            dome_list[i] = f"node {dome_list[i]} fix pp"
        elif 0 < i < 20:
            dome_list[i] = f"{dome_list[i]} fix pp"
    return dome_list


def create_domes(height, dome_type):
    def vert_cord_list(dome_type, height, param):
        def z_y(num, length=1, multiply=-1):
            x = round(length*math.sin(math.radians(num)),4)
            z = round(length*math.cos(math.radians(num)),4)*multiply
            return x, 0, z

        def coordinates(elem, start=0, end=360):
            x_y = []
            for degree in range(start, end, 18):
                value = [z_y(degree, elem[0], 1)[2], z_y(degree, elem[0], 1)[0], elem[2]]
                x_y.append(value)
            return x_y

        len_dict = {}
        for num in np.arange(0, 91, 90/8):
            if num == 0.0 or num == 90.0:
                len_dict[num] = z_y(num)
            else:
                len_dict[num] = z_y(num-param)

        all_list = [list(len_dict[0])]
        if dome_type.lower() == "schwedler" or dome_type.lower() == "zebrowa":
            for elem in list(len_dict.keys())[1:-1]:
                all_list.extend(coordinates(len_dict[elem]))
            all_list.extend(coordinates(len_dict[90]))
        else:
            for num, elem in enumerate(list(len_dict.keys())[1:], start=1):
                if not num % 2:
                    all_list.extend(coordinates(len_dict[elem], -9, 360-9))
                else:
                    all_list.extend(coordinates(len_dict[elem]))
        all_list.sort(key=lambda x: x[2], reverse=True)
        for elem in all_list:
            for i in range(len(elem)):
                elem[i] = round(elem[i]*height, 4)
        return all_list
    
    dome_dict = {}
    for num in range (-2,3):
        dome_dict[num] = vert_cord_list(dome_type, height, num)
    return dome_dict


def create_changed_domes(dome_list):
    def return_number(param):
        param = param*2
        if param < 20:
            return 20
        for num in [elem for elem in range(20, 161, 20)]:
            if num <= param < num+20:
                return num
            if param > 160:
                return 140

    main_dict = {}
    for num in range(-2,3):
        for param in np.arange(90/8, 90, 90/8):
            val = return_number(param)
            main_dict[f"{param}_{num}"] = dome_list[0][:val] + dome_list[num][val:val+20] + dome_list[0][val+20:]
    return main_dict


def prog_ase(number, load_num):
    docstring = f"""+prog ase urs:{number}
head obliczenia
syst prob th3
lc {load_num}
end\n"""
    return docstring

def prog_sofiload(number, load_num, force_name, description):
    docstring = f"""+prog sofiload urs:{number}
head loads
lc {load_num} titl {force_name}
{description}
end\n"""
    return docstring

def start_text(Name, Steel, Diameter, Thinness):
    text = f"""$ Dome {Name}
+prog aqua urs:1
head Cross-sections & Materials
echo full
$ Standars/normes
norm dc en ndc 1993-2005 coun 00 unit 5  $ unit sets AQUA-pomoc strona 3-2
$ Materials
stee no 1 type s clas {Steel} gam 0 $ stal
$ Cross-section
scit no 1  d {Diameter} t {Thinness} mno 1
end
+prog sofimsha urs:2
head Geometry
syst 3d
echo full
"""
    return text

def end_text(vert_force, snow_force): 
    load_text = f"""end\n
{prog_sofiload(3, 1, "constant_load", "node no 161 type pzz p1 0.0001")}
{prog_sofiload(4, 11, "vertical_force", f"node no 161 type pzz p1 {vert_force}")}
{prog_sofiload(5, 2, "snow", f"quad from 1 to 9999 type pzz p {snow_force}")}
{prog_ase(6, 1)}
{prog_ase(7, 2)}
{prog_ase(8, 11)}"""
    return load_text


def list_of_joined_vertices(dome_list):
    num_vertex = re.compile(r'\d{1,3} ne \d{1,3}')
    ver_list = []
    for elem in dome_list:
        ver_list.append((num_vertex.findall(elem)[0].replace(" ne", "")).split(" "))
    return ver_list


def counting(diction, elem):
    result = 0
    for i in range(3):
        result += (diction[int(elem[0])][i] - diction[int(elem[1])][i]) ** 2
    return result


def sum_of_length_count(list, diction):
    sum = 0
    for elem in list:
        sum += sqrt(counting(diction, elem))
    return round(sum)


def coord_dict(dict_list, elems):
	a1 = {}
	for num, elem in enumerate(dict_list, start=1):
		a1[num] = elem
	result = sum_of_length_count(elems, a1)
	return result


def test_length(diction, type_elems):
	test = {}
	for key in diction:
		test[key] = coord_dict(diction[key], list_of_joined_vertices(type_elems))
	return test


def create_dat(dome_name, coord, beam_elem, quad_elem):
    def write_elems(elem_list, beg_text):
        f.writelines(f"{beg_text}\n")
        for i in elem_list:
            f.writelines(f"{i}\n")

    value = test_length(coord, beam_elem)
    if not os.path.exists(f"{dome_name}"):
        os.makedirs(f"{dome_name}")
    for key in coord.keys():
        with open(os.path.join(dome_name, f"{key}.dat"), "w") as f:
            f.writelines(start_text(dome_name, Steel, Diameter, Thinness))
            write_elems(change_dome_list_to_teddy(coord[key]), "$ Verices definition")
            write_elems(beam_elem, "$ Beam definition")
            write_elems(quad_elem, "$ Quad definition") 
            f.writelines(end_text(vert_force, snow_force))
    return value


HEIGHT = 10         # m
Steel = 235         # MPa
Diameter = 133      # mm
Thinness = 10       # mm
vert_force = 2513   # kN
snow_force = 10     # kN

zebrowa_total_length = create_dat("zebrowa", create_changed_domes(create_domes(HEIGHT, "schwedler")), beam_schwedler()[:300], quad_zebrowa())
schwedler_total_length = create_dat("schwedler", create_changed_domes(create_domes(HEIGHT, "schwedler")), beam_schwedler(), quad_schwedler())
lamell_total_length = create_dat("lamell", create_changed_domes(create_domes(HEIGHT, "lamell")), beam_lamell(), quad_lamell())
