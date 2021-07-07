def fnames(param, sum):
    for num in range(param-19, param+21):
        if num < param+1:
            if num != param:
                print(f"quad no {100+sum} n1 {num} n2 {num+1} n3 {num+20} mno 1 posi cent t 1")
                sum += 1
            else:
                print(f"quad no {100+sum} n1 {num} n2 {num-19} n3 {num+20} mno 1 posi cent t 1")
                sum += 1
        else:
            if num != param+1:
                print(f"quad no {100+sum} n1 {num-20} n2 {num} n3 {num-1} mno 1 posi cent t 1")
                sum += 1
            else:
                print(f"quad no {100+sum} n1 {num-20} n2 {num} n3 {num+19} mno 1 posi cent t 1") 
                sum += 1


def snames(param, sum):
    for num in range(param-19, param+21):
        if num < param+1:
            if num != param:
                print(f"quad no {100+sum} n1 {num} n2 {num+1} n3 {num+21} mno 1 posi cent t 1")
                sum += 1
            else:
                print(f"quad no {100+sum} n1 {num} n2 {num-19} n3 {num+1} mno 1 posi cent t 1")
                sum += 1
        else:
            if num != param+1:
                print(f"quad no {100+sum} n1 {num-21} n2 {num} n3 {num-1} mno 1 posi cent t 1")
                sum += 1
            else:
                print(f"quad no {100+sum} n1 {num-1} n2 {num} n3 {num+19} mno 1 posi cent t 1") 
                sum += 1
    

def lnames(param):
    for num in range(param+1, param+20):
	    print(f"quad no {340+num} n1 {num} n2 {1+num} n3 161 mno 1 posi cent t 1")
    if num < 160:
        print(f"quad no {341+num} n1 {num+1} n2 {num-18} n3 161 mno 1 posi cent t 1")

# test1 = 1
# for num in range(20,140,40):
#     fnames(num, test1)
#     snames(num+20, test1+40)
#     test1 += 80
# fnames(140, 341)
# lnames(140)


def vert_names(param, sum):
    for num in range(param, param+121, 20):
        print(f"quad no {sum} n1 {num} n2 {num+19} n3 {num-1} mno 1 posi cent t 1")
        sum += 1
        print(f"quad no {sum} n1 {num} n2 {num+20} n3 {num+19} mno 1 posi cent t 1")
        sum += 1


def vert_names2(param, sum):
    for num in range(param, param+121, 20):
        print(f"quad no {sum} n1 {num} n2 {num+21} n3 {num+20} mno 1 posi cent t 1")
        sum += 1
        print(f"quad no {sum} n1 {num} n2 {num+1} n3 {num+21} mno 1 posi cent t 1")
        sum += 1

def vert_names201(param, sum):
    for num in range(param, param+121, 20):
        print(f"quad no {sum} n1 {num} n2 {num+1} n3 {num+20} mno 1 posi cent t 1")
        sum += 1
        print(f"quad no {sum} n1 {num} n2 {num-19} n3 {num+1} mno 1 posi cent t 1")
        sum += 1

def vert_names202(param, sum):
    for num in range(param, param+121, 20):
        print(f"quad no {sum} n1 {num} n2 {num+20} n3 {num+19} mno 1 posi cent t 1")
        sum += 1
        print(f"quad no {sum} n1 {num} n2 {num+19} n3 {num-1} mno 1 posi cent t 1")
        sum += 1

# summary = 1
# for num in range(2,19,2):
#     vert_names(num, summary)
#     summary += 14
#     vert_names2(num, summary)
#     summary += 14

# vert_names201(20,summary)
# summary += 14
# vert_names202(20,summary)
# summary += 14


# for num in range(141,160):
#     print(f"quad no {summary} n1 {num} n2 {num+1} n3 161 mno 1 posi cent t 1")
#     summary += 1
#     if num == 159:
#         print(f"quad no {summary} n1 160 n2 141 n3 161 mno 1 posi cent t 1")



def zebrowa_poles(param, sum):
    for num in range(param,141):
        if not num % 20 ==0:
            print(f"quad no {sum} n1 {num} n2 {num+1} n3 {num+21} n4 {num+20} mno 1 posi cent t 1")
            sum +=1
        else:
            print(f"quad no {sum} n1 {num} n2 {num-19} n3 {num+1} n4 {num+20} mno 1 posi cent t 1")
            sum +=1


aa = 141
zebrowa_poles(1,1)
for num in range(141,160):
    print(f"quad no {aa} n1 {num} n2 {num+1} n3 161 mno 1 posi cent t 1")
    aa += 1
    if num == 159:
        print(f"quad no {aa} n1 160 n2 141 n3 161 mno 1 posi cent t 1")