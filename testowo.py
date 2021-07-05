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

test1 = 1
for num in range(20,140,40):
    fnames(num, test1)
    snames(num+20, test1+40)
    test1 += 80
fnames(140, 341)
lnames(140)