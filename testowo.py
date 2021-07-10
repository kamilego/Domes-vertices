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


    a = []
    test1 = 1
    for num in range(20, 140, 40):
        # fnames
        a.extend(all_names(num, test1, 20, 20))
        # snames
        a.extend(all_names(num+20, test1+40, 21, 1))
        test1 += 80
    # fnames
    a.extend(all_names(140, 341, 20, 20))
    a.extend(lnames(140))
    return a

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

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

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

