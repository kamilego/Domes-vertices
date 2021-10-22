import os
import math
from math import sqrt
import re


# function returns quads for lamella dome
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

    quad_lam_list = []
    summary = 1
    for num in range(20, 140, 40):
        quad_lam_list.extend(all_names(num, summary, 20, 20))
        quad_lam_list.extend(all_names(num+20, summary+40, 21, 1))
        summary += 80
    quad_lam_list.extend(all_names(140, 241, 20, 20))
    quad_lam_list.extend(final_join(281))
    add_teddy_elem(quad_lam_list, "quad no")
    return quad_lam_list

# function returns top quads for all domes
def final_join(summary):
    small_list = []
    for num in range(141,160):
        small_list.append(f"{summary} n1 {num} n2 161 n3 {num+1} mno 1 posi cent t 1")
        summary += 1
        if num == 159:
            small_list.append(f"{summary} n1 160 n2 161 n3 141 mno 1 posi cent t 1")
    return small_list


# function returns quads for schwedler dome
def quad_schwedler():
    def final_vert_names(param, sum, a1, a2, a3, a4):
        vert_list = []
        for num in range(param, param+121, 20):
            vert_list.append(f"{sum} n1 {num} n2 {num+a2} n3 {num+a1} mno 1 posi cent t 1")
            sum += 1
            vert_list.append(f"{sum} n1 {num} n2 {num+a4} n3 {num+a3} mno 1 posi cent t 1")
            sum += 1
        return vert_list

    quad_sch_list = []
    summary = 1
    for num in range(2,19,2):
        quad_sch_list.extend(final_vert_names(num, summary, 19, -1, 20, 19))
        summary += 14
        quad_sch_list.extend(final_vert_names(num, summary, 21, 20, 1, 21))
        summary += 14

    quad_sch_list.extend(final_vert_names(20, summary, 1, 20, -19, 1))
    summary += 14
    quad_sch_list.extend(final_vert_names(20, summary, 20, 19, 19, -1))
    summary += 14

    quad_sch_list.extend(final_join(summary))
    add_teddy_elem(quad_sch_list, "quad no")
    return quad_sch_list


# function returns quads for zebrowa dome
def quad_zebrowa():
    def zebrowa_poles(param, sum):
        zebro_list = []
        for num in range(param, 141):
            if not num % 20 == 0:
                zebro_list.append(f"{sum} n1 {num} n2 {num+20} n3 {num+21} n4 {num+1} mno 1 posi cent t 1")
                sum +=1
            else:
                zebro_list.append(f"{sum} n1 {num} n2 {num+20} n3 {num+1} n4 {num-19} mno 1 posi cent t 1")
                sum +=1
        return [zebro_list, sum]
    
    quad_zeb_list = zebrowa_poles(1, 1)
    quad_zeb_list[0].extend(final_join(zebrowa_poles(1, 1)[1]))
    add_teddy_elem(quad_zeb_list[0], "quad no")
    return quad_zeb_list[0]


# function returns top beam elems for all domes
def dome_join(param, count, impr, step, plus, sp1, sp2, sp3, sp4):
    join_list = []
    for num in range(param, param+impr, step):
        if num < param+plus:
            join_list.append(f"{count} na {num} ne {num+sp1} ncs 1 div 5")
            count += 1
        else:
            join_list.append(f"{count} na {num} ne {(num-sp2)*sp3+161*sp4} ncs 1 div 5")
    return join_list


# function changes values to teddy data
def add_teddy_elem(dome_list, elem_type):
    for i in range(len(dome_list)):
        if i == 0:
            dome_list[0] = f"{elem_type} {dome_list[0]}"


# function returns beam elems for all domes
def domes_sticks(param, count, add, step, var, sp1, sp2):
    sticks_list = []
    for num in range(param, param+add, step):
        if num < param+var:
            sticks_list.append(f"{count} na {num} ne {num+20+sp1} ncs 1 div 5")
            count += 1
            sticks_list.append(f"{count} na {num+20+sp1} ne {num+step} ncs 1 div 5")
            count += 1
        else:
            sticks_list.append(f"{count} na {num} ne {num+sp2} ncs 1 div 5")
            count += 1
            sticks_list.append(f"{count} na {num+sp2} ne {num-add+1} ncs 1 div 5")
            count += 1
    return sticks_list


# function returns beam elems for lamella domes
def beam_lamell():
    beam_lam_list = []
    for num, param in enumerate([num for num in range(1, 142, 20)], start=1):
        if param < 141:
            if num % 2 == 0:
                beam_lam_list.extend(domes_sticks(param, param*2 - 1, add=20, step=1, var=19, sp1=1, sp2=1))
            else:
                beam_lam_list.extend(domes_sticks(param, param*2 - 1, add=20, step=1, var=19, sp1=0, sp2=20))
        else:
            for num in range(param, param+20):
                beam_lam_list.append(f"{num+140} na {num} ne 161 ncs 1 div 5")
    for num in range(21, 142, 20):
        beam_lam_list.extend(dome_join(num, count=280+num, impr=20, step=1, plus=19, sp1=1, sp2=19, sp3=1, sp4=0))
    add_teddy_elem(beam_lam_list, "beam no")
    return beam_lam_list


# function returns beam elems for schwedler domes
def beam_schwedler():
    beam_sch_list = []
    for num in range(1, 21):
        beam_sch_list.extend(dome_join(num, count=-7+num*8, impr=141, step=20, plus=121, sp1=20, sp2=161, sp3=0, sp4=1))
    for num in range(21, 142, 20):
        beam_sch_list.extend(dome_join(num, count=140+num, impr=20, step=1, plus=19, sp1=1, sp2=19, sp3=1, sp4=0))
    for num, param in enumerate([num for num in range(2, 141, 20)], start=1):
        beam_sch_list.extend(domes_sticks(param, 299+param, add=19, step=2, var=17, sp1=1, sp2=1))
    add_teddy_elem(beam_sch_list, "beam no")
    return beam_sch_list


# function returns list with changed data to teddy program
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


# function returns diction with coordinates for all levels
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
        ver_num = 0.0
        for _ in range(9):
            if ver_num == 0.0 or ver_num == 90.0:
                len_dict[ver_num] = y_z(ver_num)
                ver_num += 11.25
            else:
                len_dict[ver_num] = y_z(ver_num-param)
                ver_num += 11.25

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


# function changes vertices values for certain levels
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
        param = 11.25
        for _ in range(6):
            val = return_number(param)
            main_dict[f"{param}_{num}"] = dome_list[0][:val] + dome_list[num][val:val+20] + dome_list[0][val+20:]
            param += 11.25
    return main_dict


# function returns ase function to count loads
def prog_ase(number, load_num, description):
    docstring = f"""+prog ase urs:{number}
head obliczenia
lc {load_num}
{description}
end\n"""
    return docstring


# function returns sofiload function to set load value
def prog_sofiload(number, load_num, force_name, description):
    docstring = f"""+prog sofiload urs:{number}
head loads
lc {load_num} titl {force_name}
{description}
end\n"""
    return docstring


# function returns beggining of teddy script 
def start_text(Name, Steel, Diameter, Thinness, length):
    text = f"""$ Dome {Name}
$ total lenght {length}
+prog aqua urs:1
head Cross-sections & Materials
echo full
$ Standars/normes
norm dc en ndc 1993-2005 coun 00 unit 5  $ unit sets AQUA-pomoc strona 3-2
$ Materials
stee no 1 type s clas {Steel} gam 0 $ stal
stee no 999 type s clas 235
$ Cross-section
scit no 1 d {Diameter} t {Thinness} mno 999
end
+prog sofimsha urs:2
head Geometry
syst 3d
echo full\n
"""
    return text


# function replaces unnecessary elements
def change_string(string):
    string = str(string).replace("[", "").replace("]", "").replace("'", "").replace(r"\\", r"\n")
    return string


# fuction returns averange value
def middle_func(e1, e2, num):
    return [round((e1[num]+e2[num])/2, 3)]


# fucntion changes direction for loads definiotion
def change_direction(elem, elem2):
    middle = []
    for i in range(3):
        middle.extend(middle_func(elem, elem2, i))
    return middle


# function returns are definition for pressure load
def lammel(dict_list, num, load_1, load_2, param1, param2, param3, state=1):
    if state == 1:
        state = change_string(dict_list[num+param1])
    else:
        state = change_string(state)
    text = f"""area ref qgrp type pzz p1 {load_1} x1 {state} $$
        p2 {load_1} x2 {change_string(dict_list[num+param2])} $$
        p3 {load_2} x3 {change_string(dict_list[num+param3])}"""
    return text


# function returns list with loads
def load_lamell(dict_list, node, step, load_1, load_2, p1, p2):
    load_list = []
    for num in range(node, node+step):
        load_list.append(lammel(dict_list, num+p1, load_2, load_1, -1, 0, p2))
    return load_list

# function returns list with loads
def added_vert(dict_list, num, l1, l2, l3):
    load_list = []
    load_list.append(lammel(dict_list, num, l1, l2, 38, 19, -1))  # 160, 141
    load_list.append(lammel(dict_list, num, l2, l3, -1, 18, -2))  # 121, 140, 120
    load_list.append(lammel(dict_list, num, l2, l1, -1, 18, 38))  # 121, 140, 160
    load_list.append(lammel(dict_list, num, l3, l2, -21, -2, -1)) # 121, 101, 120
    return load_list


# function returns list with loads
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


# function returns list with loads
def unique_quads(dict_list, num, load_1, load_2, load_3, step):
    load_list = []
    for x, y in zip([load_2, load_3], [20, -20]):
        load_list.append(lammel(dict_list, num, load_1, x, -1, step, y, change_direction(dict_list[num])))
    return load_list


# function returns list with loads
def final_lamell_load(diction, num, c1, c2, d1, d2, l1, l2, l3, l4, l5):
    load_list = []
    for x, y, z ,k in zip([num, num, num+40, num+40], [l5, l2, l2, l4], [l1, l1, l3, l3], [-21, 19, -21, 19]):
        load_list.extend(load_lamell(diction, x, c1, y, z, 0, k))
    for x, y, z ,k in zip([num-20, num+20, num+20, num+60], [l1, l1, l3, l3], [l5, l2, l2, l4], [20, -20, 20, -20]):
        load_list.extend(load_lamell(diction, x, c2, y, z, 0, k))
    for x, y, z, k in zip([101, 111, 101, 111],[l3, l3, l1, l1],[d1, d2, d1, d2],[20, 20, -20, -20]):
        load_list.extend([lammel(diction, x, l4, y, -1, z, k, change_direction(diction[x], diction[x-1]))]) #top 
    for x, y, z, k in zip([151, 141, 151, 141],[l3, l3, l5, l5],[d2, d1, d2, d1],[-20, -20, 9, 19]):
        load_list.extend([lammel(diction, x, l4, y, -1, z, k, change_direction(diction[x], diction[x-1]))]) #top
    if num == 92:
        for x, y, z, k in zip([121, 81], [l4, l2], [l3, l1] ,[l2, l5]):
            load_list.extend(added_vert(diction, x, y, z, k))
        load_list.extend([lammel(diction, 160, l4, l5, -1, -20, 0)])
        for x, y, z, k in zip([121, 121, 81, 81], [l3, l3, l1, l1], [l4, l2, l2, l5], [19, -21, 19, -21]):
            load_list.extend([lammel(diction, x, y, z, -1, 0, k)])
        load_list.extend(extend_list(diction, l4, l2, 8, 152, 160))
    else:
        load_list.extend(extend_list(diction, l4, l2, 18, 142, 151))
    return load_list


# function returns list with loads
def extend_list(op, load_1, load_2, step, num1, num2):
    ext_list = []
    for n in range(num1, num2):
        ext_list.extend([lammel(op, n, load_1, load_2, -1, 0, step)])
        step -= 1
    return ext_list    


# function returns text with loads values
def end_text(vert_force):
    load_text = f"""{prog_sofiload(1, 1, "constant_load", "node no 161 type pzz p1 0.0001")}
{prog_sofiload(2, 2, "vertical_force", f"node no 161 type pzz p1 {vert_force}")}
{prog_ase(1, "1,2,3,4,5", "")}
{prog_ase(12, "66 dlz 1.35 titl komb_SGN", "lcc 3,4,5 fact 1.5")}
{prog_ase(13, "67 dlz 1.0 titl komb_SGU", "lcc 3,4,5 fact 1.0")}"""
    return load_text


# function returns diction with beam numbers
def create_beam_dict(beam_list, vert_list):
	beam_dict = {}
	for elem in beam_list:
		small_list = []
		for i in elem.split(" "):
			if i.isnumeric() == True:
				small_list.append(int(i))
		beam_dict[small_list[0]] = [vert_list[small_list[1]-1], vert_list[small_list[2]-1]]
	return beam_dict


# function creates freeze load case list
def return_freeze_beam_coord(beam_dict, start, step):
	coords = []
	for num in range(start, start+step+1):
		coords.append(f"line ref bgrp type pzz p1 {freeze} x1 {change_string(beam_dict[num][0])} x2 {change_string(beam_dict[num][1])}")
	return coords

# function return freeze load cases
def freeze_load(beam_dict, num1, num2, step, sum):
    freeze_list = []
    for num in range(num1, num2, step):
        freeze_list.extend(return_freeze_beam_coord(beam_dict, num, sum))
    return freeze_list


# function return freeze dome load cases
def schwedler_freeze(beam_list, vert_list, dome_name):
    freeze_list = []
    freeze_list.extend(freeze_load(create_beam_dict(beam_list, vert_list), 173, 254, 20, 5))
    freeze_list.extend(freeze_load(create_beam_dict(beam_list, vert_list), 97, 146, 8, 4))
    if dome_name == "schwedler":
        freeze_list.extend(freeze_load(create_beam_dict(beam_list, vert_list), 97, 146, 8, 4))
        return freeze_list
    else:
        return freeze_list


# function return freeze dome load cases
def dome_load_freeze(beam_list, vert_list, dome_name):
    if dome_name == "lamell":
        freeze_list = []
        for x, y in zip([27, 66], [188, 147]):
            freeze_list.extend(freeze_load(create_beam_dict(beam_list, vert_list), x, y, 80, 11))
        freeze_list.extend(freeze_load(create_beam_dict(beam_list, vert_list), 313, 394, 40, 6))
        freeze_list.extend(freeze_load(create_beam_dict(beam_list, vert_list), 334, 294, 40, 5))
        return freeze_list
    else:
        return schwedler_freeze(beam_list, vert_list, dome_name)


# function return snow load cases
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
        force_list = []
        for num in range(number, number+10):
            if num not in [num for num in range(80, 161, 20)]:
                force_list.append(area_load_string(diction, num, load_1, load_2, a1, a3, a4, a5, a6))
            else:
                force_list.append(area_load_string(diction, num, load_1, load_2, a2, a1, a4, a5, a6))
        return force_list

    tops_values = []
    v = [0.6, 0.6, 0.6, 0.6 , 0.6]
    values = [val*multiply for val in v]
    levels = [num for num in range(no_side, no_side*2+1, 20)]
    for num, elem in enumerate(levels):
        tops_values.append([elem, values[num], values[num+1]])
    snow_lista = []
    for elem in tops_values:
        snow_lista.extend(force_snow_load(diction, elem[0], elem[1], elem[2], 0, 20, 20, 19, 1, 0))
    snow_lista.extend(force_snow_load(diction, no_side+80, 0.6*multiply, 0, 0, 20, 0, 0, 0, 1))
    return snow_lista


# fucntion searches for digits and returns list of them 
def list_of_joined_vertices(dome_list):
    num_vertex = re.compile(r'\d{1,3} ne \d{1,3}')
    ver_list = []
    for elem in dome_list:
        ver_list.append((num_vertex.findall(elem)[0].replace(" ne", "")).split(" "))
    return ver_list


# function returns distance between two vertices
def counting(diction, elem):
    result = 0
    for i in range(3):
        result += (diction[int(elem[0])][i] - diction[int(elem[1])][i]) ** 2
    return result


# function counts total lenght elems
def sum_of_length_count(list, diction):
    sum = 0
    for elem in list:
        sum += sqrt(counting(diction, elem))
    return round(sum)


# function returns result of couting
def coord_dict(dict_list, elems):
	small_dict = {}
	for num, elem in enumerate(dict_list, start=1):
		small_dict[num] = elem
	result = sum_of_length_count(elems, small_dict)
	return result

# function returns total lenght elems
def total_length(diction, type_elems):
	total_dict = {}
	for key in diction:
		total_dict[key] = coord_dict(diction[key], list_of_joined_vertices(type_elems))
	return total_dict


# function returns snow load
def snow_func(start, stop, step, s1, p2):
    wind_list = []
    for num in range(start, stop, step):
        wind_list.append(f"quad from {num} to {num+s1} type pzz p {p2}")
    return wind_list


# function returns snow load
def zebr_sched_snow(dome_name):
    snow_load = []
    if dome_name == "zebrowa":
        snow_load.extend(snow_func(61, 142, 20, 9, 0.6))
        snow_load.extend(snow_func(71, 152, 20, 9, 1.2))
        return snow_load
    else:
        snow_load.extend(snow_func(7, 135, 14, 7, 0.6))
        snow_load.extend(snow_func(147, 275, 14, 7, 1.2))
        snow_load.append(f"quad from 281 to 290 type pzz p 0.6")
        snow_load.append(f"quad from 291 to 300 type pzz p 1.2")
        return snow_load


# function returns snow load
def dome_load_snow(diction_list, name, s):
    a = snow/2
    load_snow_list = []
    if name == "lamell":
        load_snow_list.extend(final_lamell_load(diction_list, 82, 10, 9, 0, -1, a, a, a, a, a))
        load_snow_list.extend(final_lamell_load(diction_list, 92, 8, 8, -1, 0, s, s, s, s, s))
        return load_snow_list
    else:
        return zebr_sched_snow(name)


# function returns zebrowa dome load
def dome_wind(dome_name, start, stop, step, s1, s2, p1, p2, beg, end):
    wind_list = [f"quad from {beg} to {end} type pyy p {p1}"]
    for num in range(start, stop, step):
        wind_list.append(f"quad from {num} to {num+s1} type pyy p {p2}")
        if dome_name == "zebrowa":
            wind_list.append(f"quad from {num-s2} to {num-1} type pyy p {p1}")
            wind_list.append(f"quad from {num+s1+1} to {num+s1+2} type pyy p {p1}")
        else:
            wind_list.append(f"quad from {num+s1+1} to {num+s1+4} type pyy p {p1}")
    if dome_name == "schwedler":
        wind_list.append(f"quad from 253 to 300 type pyy p {p1}")
    return wind_list


# function returns dome wind load case
def dome_load_wind(dome_name):
    w1 = round(wind*0.8, 2)
    w2 = round(wind*1.2, 2)
    if dome_name == "zebrowa":
        return dome_wind("zebrowa", 13, 94, 20, 5, 12, w2, w1, 101, 160)
    elif dome_name == "lamell":
        return lamel_wind()
    else:
        return dome_wind("schwedler", 169, 240, 14, 9, 10, w2, w1, 1, 168)


# funtion returns quad numbers for lamella wind load 
def lamel_wind():
    wind_list = ["quad from 1 to 13 type pyy p 1.72", "quad from 200 to 300 type pyy p 1.72"]
    x = [14, 75, 94, 155, 174]
    y = [34, 53, 114, 133, 194]
    for a, b in zip(x,y):
        wind_list.append(f"quad from {a} to {a+4} type pyy p 1.14")
        wind_list.append(f"quad from {b} to {b+5} type pyy p 1.14")
    for i in range(len(wind_list)):
	    wind_list[i] = wind_list[i].split(" ")
    for i in range(len(wind_list)):
        wind_list[i][2] = int(wind_list[i][2])
    wind_list.sort(key=lambda x: x[2])
    for i in range(len(wind_list)):
        wind_list[i][2] = str(wind_list[i][2])
        wind_list[i] = " ".join(wind_list[i])
    xy = []
    for elem in wind_list:
        for i in elem.split(" "):
            if i.isnumeric() == True:
                xy.append(int(i))
    xy = xy[3:-3]
    for num in range(len(xy)):
        if num % 2 == 0:
            xy[num] = xy[num]+1
        else:
            xy[num] = xy[num]-1
    for num in range(0, len(xy)-1, 2):
        wind_list.append(f"quad from {xy[num]} to {xy[num+1]} type pyy p 1.72")
    return wind_list


# function return value of all elements that dome consists of and created .dat files
def create_dat(dome_name, coord, beam_elem, quad_elem):
    def write_elems(elem_list, beg_text, end_text=""):
        f.writelines(f"{beg_text}\n")
        for i in elem_list:
            f.writelines(f"{i}\n")
        f.writelines(f"{end_text}\n")

    value = total_length(coord, beam_elem)
    if not os.path.exists(f"{dome_name}"):
        os.makedirs(f"{dome_name}")
    for key in coord.keys():
        with open(os.path.join(dome_name, f"{key}.dat"), "w") as f:
            f.writelines(start_text(dome_name, Steel, Diameter, Thinness, value[key]))
            write_elems(change_dome_list_to_teddy(coord[key]), "$ Verices definition")
            for x, y in zip([beam_elem, quad_elem], ["$ Beam definition", "$ Quad definition"]):
                write_elems(x, y)
            write_elems(dome_load_snow(coord[key], dome_name, snow),"end\n$ Snow load\n+prog sofiload urs:5\nhead loads\nlc 3 titl snow", "end\n")
            write_elems(dome_load_freeze(beam_elem, coord[key], dome_name), "$ Freeze load\n+prog sofiload urs:4\nhead loads\nlc 4 titl freeze", "end\n")
            write_elems(dome_load_wind(dome_name), "$ Wind load\n+prog sofiload urs:4\nhead loads\nlc 5 titl wind", "end\n")
            f.writelines(end_text(vert_force))
    return value


# Values to be set by user
HEIGHT = 50         # m
Steel = 235         # MPa
Diameter = 108      # mm
Thinness = 9.27     # mm
snow = 1.2          # kN/m2
freeze = 0.022      # kN/mb
wind = 1.43         # kN/m2
vert_force = 2188   # kN


# dictions with total lenght values for certain dome degree change
zebrowa_total_length = create_dat("zebrowa", create_changed_domes(create_domes(HEIGHT, "schwedler")), beam_schwedler()[:300], quad_zebrowa())
schwedler_total_length = create_dat("schwedler", create_changed_domes(create_domes(HEIGHT, "schwedler")), beam_schwedler(), quad_schwedler())
lamell_total_length = create_dat("lamell", create_changed_domes(create_domes(HEIGHT, "lamell")), beam_lamell(), quad_lamell())

 
for name, dome in zip([zebrowa_total_length, schwedler_total_length, lamell_total_length], ["zebrowa", "schwedler", "lamella"]):
    print(f"total lenght for {dome}:")
    keys_list = list(name.keys())
    keys_list.sort(key=lambda x: x.split("_")[0])
    for key in keys_list:
        print(f"{key}: {name[key]}m")
