def lammel_names():
    def all_names(param, sum,  a4, a5, a1=0, a2=1, a3=19):
        lista = []
        for num in range(param-19, param+21):
            if num < param+1:
                if num != param:
                    lista.append(f"quad no {sum} n1 {num+a1} n2 {num+a2} n3 {num+a4} mno 1 posi cent t 1")
                    sum += 1
                else:
                    lista.append(f"quad no {sum} n1 {num+a1} n2 {num-a3} n3 {num+a5} mno 1 posi cent t 1")
                    sum += 1
            else:
                if num != param+1:
                    lista.append(f"quad no {sum} n1 {num-a4} n2 {num+a1} n3 {num-a2} mno 1 posi cent t 1")
                    sum += 1
                else:
                    lista.append(f"quad no {sum} n1 {num-a5} n2 {num+a1} n3 {num+a3} mno 1 posi cent t 1") 
                    sum += 1
        return lista

    def lnames(param):
        lista = []
        for num in range(param+1, param+20):
            lista.append(f"quad no {140+num} n1 {num} n2 {1+num} n3 161 mno 1 posi cent t 1")
        if num < 160:
            lista.append(f"quad no {141+num} n1 {num+1} n2 {num-18} n3 161 mno 1 posi cent t 1")
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
    return f_list

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def final_join(summary):
    small_list = []
    for num in range(141,160):
        small_list.append(f"quad no {summary} n1 {num} n2 {num+1} n3 161 mno 1 posi cent t 1")
        summary += 1
        if num == 159:
            small_list.append(f"quad no {summary} n1 160 n2 141 n3 161 mno 1 posi cent t 1")
    return small_list


def schwedler_names():
    def final_vert_names(param, sum, a1, a2, a3, a4):
        lista = []
        for num in range(param, param+121, 20):
            lista.append(f"quad no {sum} n1 {num} n2 {num+a1} n3 {num+a2} mno 1 posi cent t 1")
            sum += 1
            lista.append(f"quad no {sum} n1 {num} n2 {num+a3} n3 {num+a4} mno 1 posi cent t 1")
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
    return names_list

def zebrowa_list():
    def zebrowa_poles(param, sum):
        lista = []
        for num in range(param, 141):
            if not num % 20 ==0:
                lista.append(f"quad no {sum} n1 {num} n2 {num+1} n3 {num+21} n4 {num+20} mno 1 posi cent t 1")
                sum +=1
            else:
                lista.append(f"quad no {sum} n1 {num} n2 {num-19} n3 {num+1} n4 {num+20} mno 1 posi cent t 1")
                sum +=1
        return [lista, sum]
    
    f_list = zebrowa_poles(1, 1)
    f_list[0].extend(final_join(zebrowa_poles(1, 1)[1]))
    return f_list[0]

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def dome_join(param, count, impr, step, plus, sp1, sp2, sp3, sp4):
    lista = []
    for num in range(param, param+impr, step):
        if num < param+plus:
            lista.append(f"{count} na {num} ne {num+sp1} ncs 1")
            count += 1
        else:
            lista.append(f"{count} na {num} ne {(num-sp2)*sp3+161*sp4} ncs 1")
    return lista


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


def full_lamell():
    check_list = []
    for num, param in enumerate([num for num in range(1, 142, 20)], start=1):
        if param < 141:
            if num % 2 == 0:
                check_list.extend(domes_sticks(param, param*2 - 1, add=20, step=1, var=19, sp1=1, sp2=1))
            else:
                check_list.extend(domes_sticks(param, param*2 - 1, add=20, step=1, var=19, sp1=0, sp2=20))
        else:
            for num in range(param, param+19):
                check_list.append(f"{num+141} na {num} ne 161 ncs 1")
    for num in range(21, 142, 20):
        check_list.extend(dome_join(num, count=280+num, impr=20, step=1, plus=19, sp1=1, sp2=19, sp3=1, sp4=0))
    return check_list


def full_schwedler():
    lista = []
    for num in range(1, 21):
        lista.extend(dome_join(num, count=-7+num*8, impr=141, step=20, plus=121, sp1=20, sp2=161, sp3=0, sp4=1))
    for num in range(21, 142, 20):
        lista.extend(dome_join(num, count=140+num, impr=20, step=1, plus=19, sp1=1, sp2=19, sp3=1, sp4=0))
    for num, param in enumerate([num for num in range(2, 141, 20)], start=1):
        lista.extend(domes_sticks(param, 299+param, add=19, step=2, var=17, sp1=1, sp2=1))
    return lista


lamela = full_lamell()
schwedler = full_schwedler()
zebrowa = schwedler[:300]