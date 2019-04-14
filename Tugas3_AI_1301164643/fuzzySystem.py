import csv

def linearFunctionUp(a,b,x):
    return (x-a)/(b-a)

def linearFunctionDown(a,b,x):
    return (b-x)/(b-a)

def sangatTinggi(komp):
    if (komp >= 80):
        return 1
    elif (komp < 80) and (komp > 70):
        return linearFunctionUp(70,80,komp)
    else:
        return 0

def tinggi(komp):
    if (komp > 63) and (komp < 66):
        return linearFunctionUp(63,66,komp)
    elif (komp >= 66) and (komp <= 70):
        return 1
    elif (komp > 70) and (komp < 80):
        return linearFunctionDown(70,80,komp)
    else:
        return 0

def cukup(komp):
    if (komp > 50) and (komp < 53):
        return linearFunctionUp(50,53,komp)
    elif (komp >= 53) and (komp <= 63):
        return 1
    elif (komp > 63) and (komp < 66):
        return linearFunctionDown(63,66,komp)
    else:
        return 0

def rendah(komp):
    if (komp <= 50):
        return 1
    elif (komp > 50) and (komp < 53):
        return linearFunctionDown(50,53,komp)
    else:
        return 0

def sangatBaik(kepr):
    if (kepr > 73) and (kepr < 75):
        return linearFunctionUp(73,75,kepr)
    elif (kepr >= 75):
        return 1
    else:
        return 0

def baik(kepr):
    if (kepr > 60) and (kepr < 70):
        return linearFunctionUp(60,70,kepr)
    elif (kepr >= 70) and (kepr <= 73):
        return 1
    elif (kepr > 73) and (kepr < 75):
        return linearFunctionDown(73,75)
    else:
        return 0

def lumayan(kepr):
    if (kepr > 40) and (kepr < 50):
        return linearFunctionUp(40,50,kepr)
    elif (kepr >= 50) and (kepr <= 60):
        return 1
    elif (kepr > 60) and (kepr < 70):
        return linearFunctionDown(60,70,kepr)
    else:
        return 0

def buruk(kepr):
    if (kepr <= 40):
        return 1
    elif (kepr > 40) and (kepr < 50):
        return linearFunctionDown(40,50,kepr)
    else:
        return 0

def accepted(komp,kepr):
    A1 = min(sangatTinggi(komp),sangatBaik(kepr))
    A2 = min(sangatTinggi(komp),baik(kepr))
    A3 = min(sangatTinggi(komp),lumayan(kepr))
    A4 = min(tinggi(komp),sangatBaik(kepr))
    A5 = min(tinggi(komp),baik(kepr))
    A6 = min(tinggi(komp),lumayan(kepr))
    A7 = min(cukup(komp),sangatBaik(kepr))
    A8 = min(cukup(komp),baik(kepr))
    A9 = min(rendah(komp),sangatBaik(kepr))
    return max(A1,A2,A3,A4,A5,A6,A7,A8,A9)

def rejected(komp,kepr):
    R1 = min(sangatTinggi(komp),buruk(kepr))
    R2 = min(tinggi(komp),buruk(kepr))
    R3 = min(cukup(komp),lumayan(kepr))
    R4 = min(cukup(komp),buruk(kepr))
    R5 = min(rendah(komp),baik(kepr))
    R6 = min(rendah(komp),lumayan(kepr))
    R7 = min(rendah(komp),buruk(kepr))
    return max(R1,R2,R3,R4,R5,R6,R7)

header = []
hasil = []
i = 0

with open('DataTugas3.csv') as rfile:
    reader = csv.reader(rfile)
    for row in reader:
        if i == 0:
            data = [row[0], row[1], row[2], row[3]]
            header.append(data)
            i = 1
        else:
            kompetensi = float(row[1])
            kepribadian = float(row[2])
            Amax = accepted(kompetensi,kepribadian)
            Rmax = rejected(kompetensi,kepribadian)
            if (Amax >= Rmax):
                data = [row[0],kompetensi,kepribadian,'Ya']
                hasil.append(data)
            else:
                data = [row[0],kompetensi,kepribadian,'Tidak']
                hasil.append(data)

wfile = open('TebakanTugas3.csv','w',newline="")
write = csv.writer(wfile)
write.writerows(header)
write.writerows(hasil)
wfile.close()