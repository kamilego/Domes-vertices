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
                    lista.append(f"{sum} n1 {num+a1} n2 {num+a4} n3 {num+a2} mno 1 posi cent t 1")
                    sum += 1
                else:
                    lista.append(f"{sum} n1 {num+a1} n2 {num+a5} n3 {num-a3} mno 1 posi cent t 1")
                    sum += 1
            else:
                if num != param+1:
                    lista.append(f"{sum} n1 {num-a4} n2 {num-a2} n3 {num+a1} mno 1 posi cent t 1")
                    sum += 1
                else:
                    lista.append(f"{sum} n1 {num-a5} n2 {num+a3} n3 {num+a1} mno 1 posi cent t 1") 
                    sum += 1
        return lista

    f_list = []
    summary = 1
    for num in range(20, 140, 40):
        # fnames
        f_list.extend(all_names(num, summary, 20, 20))
        # snames
        f_list.extend(all_names(num+20, summary+40, 21, 1))
        summary += 80
    # fnames
    f_list.extend(all_names(140, 241, 20, 20))
    f_list.extend(final_join(281))
    add_teddy_elem(f_list, "quad no")
    return f_list

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def final_join(summary):
    small_list = []
    for num in range(141,160):
        small_list.append(f"{summary} n1 {num} n2 161 n3 {num+1} mno 1 posi cent t 1")
        summary += 1
        if num == 159:
            small_list.append(f"{summary} n1 160 n2 161 n3 141 mno 1 posi cent t 1")
    return small_list


def quad_schwedler():
    def final_vert_names(param, sum, a1, a2, a3, a4):
        lista = []
        for num in range(param, param+121, 20):
            lista.append(f"{sum} n1 {num} n2 {num+a2} n3 {num+a1} mno 1 posi cent t 1")
            sum += 1
            lista.append(f"{sum} n1 {num} n2 {num+a4} n3 {num+a3} mno 1 posi cent t 1")
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
            if not num % 20 == 0:
                lista.append(f"{sum} n1 {num} n2 {num+20} n3 {num+21} n4 {num+1} mno 1 posi cent t 1")
                sum +=1
            else:
                lista.append(f"{sum} n1 {num} n2 {num+20} n3 {num+1} n4 {num-19} mno 1 posi cent t 1")
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
            lista.append(f"{count} na {num} ne {num+sp1} ncs 1 div 5")
            count += 1
        else:
            lista.append(f"{count} na {num} ne {(num-sp2)*sp3+161*sp4} ncs 1 div 5")
    return lista

def add_teddy_elem(dome_list, elem_type):
    for i in range(len(dome_list)):
        if i == 0:
            dome_list[0] = f"{elem_type} {dome_list[0]}"

def domes_sticks(param, count, add, step, var, sp1, sp2):
    lista = []
    for num in range(param, param+add, step):
        if num < param+var:
            lista.append(f"{count} na {num} ne {num+20+sp1} ncs 1 div 5")
            count += 1
            lista.append(f"{count} na {num+20+sp1} ne {num+step} ncs 1 div 5")
            count += 1
        else:
            lista.append(f"{count} na {num} ne {num+sp2} ncs 1 div 5")
            count += 1
            lista.append(f"{count} na {num+sp2} ne {num-add+1} ncs 1 div 5")
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
                check_list.append(f"{num+140} na {num} ne 161 ncs 1 div 5")
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
    dome_list_copy = dome_list.copy()
    for i in range(len(dome_list_copy)):
        dome_list_copy[i] = str(dome_list_copy[i]).replace("[", "").replace("]","")
        dome_list_copy[i] = f"{i+1} {dome_list_copy[i]}"
        if i == 0:
            dome_list_copy[i] = f"node {dome_list_copy[i]} fix pp"
        elif 0 < i < 20:
            dome_list_copy[i] = f"{dome_list_copy[i]} fix pp"
    return dome_list_copy


def create_domes(height, dome_type):
    def vert_cord_list(dome_type, height, param):
        def y_z(num, length=1, multiply=-1):
            y = round(length*math.sin(math.radians(num)),4)
            z = round(length*math.cos(math.radians(num)),4)*multiply
            return 0, y, z

        def coordinates(elem, start=0, end=360):
            x_y = []
            for degree in range(start, end, 18):
                value = [y_z(degree, elem[1], 1)[2], y_z(degree, elem[1], 1)[1], elem[2]]
                x_y.append(value)
            return x_y

        len_dict = {}
        for num in np.arange(0, 91, 90/8):
            if num == 0.0 or num == 90.0:
                len_dict[num] = y_z(num)
            else:
                len_dict[num] = y_z(num-param)

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
stee no 999 type s clas 235
$ Cross-section
scit no 1  d {Diameter} t {Thinness} mno 999
end
+prog sofimsha urs:2
head Geometry
syst 3d
echo full
"""
    return text


def change_string(string):
    string = str(string).replace("[", "").replace("]", "").replace("'", "").replace(r"\\", r"\n")
    return string


def change_direction(elem):
    return [elem[0], 0, elem[2]]


def lammel(dict_list, num, load_1, load_2, param1, param2, param3, state=1):
    if state == 1:
        state = change_string(dict_list[num+param1])
    else:
        state = change_string(state)
    text = f"""area ref qgrp type pzz p1 {load_1} x1 {state} $$
        p2 {load_1} x2 {change_string(dict_list[num+param2])} $$
        p3 {load_2} x3 {change_string(dict_list[num+param3])}"""
    return text


def load_lamell(dict_list, node, step, load_1, load_2, p1, p2, p3, p4):
    load_list = []
    for num in range(node, node+step):
        load_list.append(lammel(dict_list, num+p1, load_2, load_1, -1, 0, p3))
        if num < node+9:
            load_list.append(lammel(dict_list, num+p2, load_1, load_2, -1, 0, p4))
    return load_list


def added_vert(dict_list, num, l1, l2, l3):
    load_list = []
    load_list.append(lammel(dict_list, num, l1, l2, 38, 19, -1))  # 160, 141
    load_list.append(lammel(dict_list, num, l2, l3, -1, 18, -2))  # 121, 140, 120
    load_list.append(lammel(dict_list, num, l2, l1, -1, 18, 38))  # 121, 140, 160
    load_list.append(lammel(dict_list, num, l3, l2, -21, -2, -1)) # 121, 101, 120
    return load_list


def top_load(dict_list, num, l1, l2):
    param = 19 if num == 141 else 9
    load_list = []
    for elem in range(num, num+10):
        if elem == 160:
            load_list.append(lammel(dict_list, elem, l1, l2, -1, -20, 0))
        else:
            load_list.append(lammel(dict_list, elem, l1, l2, -1, 0, param)) # 141, 142, 161
            param -= 1
    return load_list


def unique_quads(dict_list, num, load_1, load_2, load_3, step):
    load_list = []
    for _ in range(1):
        load_list.append(lammel(dict_list, num, load_1, load_2, -1, step, 19, change_direction(dict_list[num-1])))
        load_list.append(lammel(dict_list, num, load_1, load_3, -1, step, -21, change_direction(dict_list[num-1])))
    return load_list

    
def lamell_snow_load(dict_list, num, step, l1, l2, l3, l4, left):
    load_list = []
    # DRUGA STRONA
    side = 0 if left == -1 else -1
    load_list.extend(load_lamell(dict_list, num, step, l4, 0, 0, 21, 20, -21))
    load_list.extend(load_lamell(dict_list, num+21, step, l4, l3, 19, 0, -20, 19))
    load_list.extend(load_lamell(dict_list, num+40, step, l2, l3, 0, 21, 20, -21))
    load_list.extend(load_lamell(dict_list, num+61, step, l2, l1, 19, 0, -20, 19))
    load_list.extend(unique_quads(dict_list, 131, l2, l1, l3, left))
    load_list.extend(unique_quads(dict_list, 91, l4, l3, 0, left))
    load_list.extend(unique_quads(dict_list, 121, l2, l1, l3, side))
    load_list.extend(unique_quads(dict_list, 81, l4, l3, 0, side))
    load_list.extend(top_load(dict_list, num+80, l1, 0))
    if left != -1:
        load_list.extend(added_vert(dict_list, 121, l1, l2, l3))
        load_list.extend(added_vert(dict_list, 81, l3, l4, 0))
    return load_list


def end_text(vert_force):
    load_text = f"""{prog_sofiload(3, 1, "constant_load", "node no 161 type pzz p1 0.0001")}
{prog_sofiload(4, 11, "vertical_force", f"node no 161 type pzz p1 {vert_force}")}
{prog_ase(7, 1)}
{prog_ase(8, 11)}
{prog_ase(9, 2)}"""
    return load_text


def snow_load(diction, no_side, multiply):
    def force_snow_load(diction, number, load_1, load_2, a1, a2, a3, a4, a5, a6):
        def area_load_string(diction, num, load_1, load_2, param1, param2, param3, area_type1, area_type2):
            text = f"""area ref qgrp type pzz p1 {load_1} x1 {change_string(diction[num-1])} $$
                p2 {load_1} x2 {change_string(diction[num-param1])} $$
                p3 {load_2} x3 {change_string(diction[(num+param2)*area_type1-(1*area_type2)])} $$
                p4 {load_2} x4 {change_string(diction[num+param3])}\n"""
            if area_type1 == 1:
                return text
            else:
                text = text[:len(text)-text[::-1].index("$$")-2] + "\n"
                return text
        lista = []
        for num in range(number, number+10):
            if num not in [num for num in range(80, 161, 20)]:
                lista.append(area_load_string(diction, num, load_1, load_2, a1, a3, a4, a5, a6))
            else:
                lista.append(area_load_string(diction, num, load_1, load_2, a2, a1, a4, a5, a6))
        return lista

    tops_values = []
    v = [0, 0.1663, 0.3689, 0.6 , 0.3059]
    values = [val*multiply for val in v]
    levels = [num for num in range(no_side, no_side*2+1, 20)]
    for num, elem in enumerate(levels):
        tops_values.append([elem, values[num], values[num+1]])
    lista = []
    for elem in tops_values:
        lista.extend(force_snow_load(diction, elem[0], elem[1], elem[2], 0, 20, 20, 19, 1, 0))
    lista.extend(force_snow_load(diction, no_side+80, 0.3059*multiply, 0, 0, 20, 0, 0, 0, 1))
    return lista


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


def snow_loads(diction_list, name):
    load_snow_list = []
    if name == "lamell":
        load_snow_list.extend(lamell_snow_load(diction_list, 71, 9, 0.6118, 1.2, 0.7378, 0.3326, 0))
        load_snow_list.extend(lamell_snow_load(diction_list, 61, 10, 0.3059, 0.6, 0.3689, 0.1663, -1))
    else:
        load_snow_list.extend(snow_load(diction_list, 61, 1))
        load_snow_list.extend(snow_load(diction_list, 71, 2))
    return load_snow_list

def create_dat(dome_name, coord, beam_elem, quad_elem):
    def write_elems(elem_list, beg_text, end_text=""):
        f.writelines(f"{beg_text}\n")
        for i in elem_list:
            f.writelines(f"{i}\n")
        f.writelines(f"{end_text}\n")

    value = test_length(coord, beam_elem)
    if not os.path.exists(f"{dome_name}"):
        os.makedirs(f"{dome_name}")
    for key in coord.keys():
        with open(os.path.join(dome_name, f"{key}.dat"), "w") as f:
            f.writelines(start_text(dome_name, Steel, Diameter, Thinness))
            write_elems(change_dome_list_to_teddy(coord[key]), "$ Verices definition")
            write_elems(beam_elem, "$ Beam definition")
            write_elems(quad_elem, "$ Quad definition")
            write_elems(snow_loads(coord[key], dome_name),"end\n$ Quad definition\n+prog sofiload urs:4\nhead loads\nlc 2 titl snow", "end\n")
            f.writelines(end_text(vert_force))
    return value


HEIGHT = 10         # m
Steel = 235         # MPa
Diameter = 133      # mma
Thinness = 10       # mm
vert_force = 2513   # kN
snow_force = 10     # kN


zebrowa_total_length = create_dat("zebrowa", create_changed_domes(create_domes(HEIGHT, "schwedler")), beam_schwedler()[:300], quad_zebrowa())
schwedler_total_length = create_dat("schwedler", create_changed_domes(create_domes(HEIGHT, "schwedler")), beam_schwedler(), quad_schwedler())
lamell_total_length = create_dat("lamell", create_changed_domes(create_domes(HEIGHT, "lamell")), beam_lamell(), quad_lamell())

