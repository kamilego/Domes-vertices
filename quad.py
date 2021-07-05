string = ''' quad no 101 n1 21 n2 40 n3 1 mno 1 posi cent t 1
        102 n1 22 n2 21 n3 2 mno 1 posi cent t 1'''

text = []

r1 = [elem for elem in range(1,21)][::-1]
r2 = [elem for elem in range(21,41)]

t_size = 1

for row in range(1,21):
    if row == 1:
        text.append("quad no 101 n1 21 n2 40 n3 1 mno 1 posi cent t 1")
    else:
        text.append("100"+str(row)+"n1 %s n2 %s n3 %s mno %s posi cent t %s" % ())
