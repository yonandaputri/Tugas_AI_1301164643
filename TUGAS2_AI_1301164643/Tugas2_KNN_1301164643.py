import pandas as pd
import math


def getClass(test,train):
    classPred = []
    K = 5
    for i in range(len(test)):
        array =[]
        label=[]
        lbl0=0
        lbl1=0
        for j in range(len(train)):
            array.append([math.sqrt(((test["atribut 1"][i]- train["atribut 1"][j])**2)+((test["atribut 2"][i]- train["atribut 2"][j])**2)+((test["atribut 3"][i]- train["atribut 3"][j])**2)+((test["atribut 4"][i]- train["atribut 4"][j])**2)),train["kelas"][j]])
        array.sort()
        for k in range(K):
            if(array[k][1]==0):
                lbl0=lbl0+1
            elif(array[k][1]==1):
                lbl1=lbl1+1
        label.append(lbl0)
        label.append(lbl1)
        classPred.append(label.index(max(label)))
    return classPred
	


# LOAD DATA
dataTest = pd.read_csv("[2019] DataTest Tugas 2 AI.csv")
dataTrain = pd.read_csv("[2019] DataTrain Tugas 2 AI.csv")

# GET CLASS FOR DATA TEST
neighbors = getClass(dataTest,dataTrain)
prediction = pd.DataFrame({"Prediksi Kelas" : neighbors, })

# MAKE A NEW FILE AND SAVE RESULTS   
prediction.to_csv('Prediksi_Tugas2AI_[1301164643].csv', index = False)