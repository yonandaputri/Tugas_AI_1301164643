import math
import numpy as np


def euclidianDist(x1, x2, x3, x4, y1, y2, y3, y4):
    return math.sqrt(math.pow((x1 - y1), 2) + math.pow((x2 - y2), 2) + math.pow((x3 - y3), 2) + math.pow((x4 - y4), 2))


def getKey(item):
    return item[0]


def voteClass(K):
    classPred = [0, 0]
    for data in K:
        classPred[int(data[0])] += 1
    return classPred.index(max(classPred))


def splitDataTrain(dtrain):
    fold = 8
    dtrain = dtrain
    panjang = int(len(dtrain) / fold)
    awal = 0
    dset = []
    for i in range(fold):
        akhir = awal + panjang
        train = dtrain[awal:akhir]
        test = []
        for i in range(len(dtrain)):
            if (i > akhir or i < awal):
                test.append(dtrain[i])
        dset.append([train, test])
        awal += panjang
    return dset


if __name__ == '__main__':

    # LOAD DATA TRAIN
    dataTrain = np.loadtxt(open("[2019] DataTrain Tugas 2 AI.csv", "rb"), delimiter=",", skiprows=1)
    arrdatatrain = [dataTrain[i] for i in range(len(dataTrain))]
    for K in range(3,41,2):
        accuracy = []
        dataSet = splitDataTrain(arrdatatrain)
        for fold in dataSet:
            output = []
            for test in fold[0]:
                data2 = test
                arrEuclidian = []
                for train in fold[1]:
                    data1 = train
                    euclid = euclidianDist(float(data2[0]), float(data1[0]), float(data2[1]), float(data1[1]),
                                         float(data2[2]), float(data1[2]), float(data2[3]), float(data1[3]))
                    arrEuclidian.append([data1[4], euclid])
                sortedEuclidian = sorted(arrEuclidian, key=lambda x: x[1])
                arrayK = sortedEuclidian[0:K]
                output.append(1 if voteClass(arrayK) is int(test[4]) else 0)
            accuracy.append(sum(output)/len(output))
        print("Accuracy K = %d :" % K,sum(accuracy)/len(accuracy))