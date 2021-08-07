import os
import numpy as np
import math


# path = r"D:\Programy\z.programowanie\test\vertices.xlsx"[:-13]
# for num in range(-2,3):
#     if num != 0:
#         if not os.path.exists(os.path.join(path, f"{num}")):
#             os.makedirs(os.path.join(path, f"{num}"))


def print_list(vert_list):
    for i in range(len(vert_list)):
        vert_list[i] = str(vert_list[i]).replace("[", "").replace("]","")

    for num, i in enumerate(vert_list, start=1):
        if num == 1:
            print("node", num, i, "fix pp")
        elif 1 < num < 21:
            print(num, i, "fix pp")
        else:
            print(num, i)


def create_domes(height, dome_type):
    def vert_cord_list(dome_type, height, param):
        def z_y(num):
            x = round(math.sin(math.radians(num)),4)
            z = round(math.cos(math.radians(num)),4)*-1
            return x, 0, z

        def coordinates(elem, start=0, end=360):
            x_y = []
            for degree in range(start, end, 18):
                value = [round(elem[0]*math.cos(math.radians(degree)), 4), round(elem[0]*math.sin(math.radians(degree)), 4), elem[2]]
                x_y.append(value)
            return x_y

        len_dict = {}
        for num in np.arange(0, 91, 90/8):
            if num == 0.0 or num == 90.0:
                len_dict[num] = z_y(num)
            else:
                len_dict[num] = z_y(num-param)

        all_list = [list(len_dict[0])]
        if dome_type == "schwedler":
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
            if not num == 0:
                main_dict[f"{num}_{param}"] = dome_list[0][:return_number(param)] + dome_list[num][return_number(param):return_number(param)+20] + dome_list[0][return_number(param)+20:]
    return main_dict



HEIGHT = 10
first_domes = create_domes(HEIGHT, "schwedler")
first_domes_dict = create_changed_domes(first_domes)
print()
lamell_domes = create_domes(HEIGHT, "lamell")
lamell_domes_dict = create_changed_domes(lamell_domes)


