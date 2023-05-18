import math as mt
import os

inputDir = os.listdir("/Users/jeffmills/PycharmProjects/EfficientKL_V1.0/Training_Data_Master/")
index = 0

for file in inputDir:
    FileSeq = list()
    if file != ".DS_Store":
        #print("FileName: "+ file)
        inpFile = "/Users/jeffmills/PycharmProjects/EfficientKL_V1.0/Training_Data_Master/"+str(file)
        with open(inpFile, "r") as inp:
            for line in inp:
                for int in line:
                    FileSeq.append(str(int))

    outputTxt = "/Users/jeffmills/PycharmProjects/EfficientKL_V1.0/LinuxDataSet/Trace" + str(index) + ".txt"
    index += 1
    with open(outputTxt, "w") as fWtxt:
        for i in range(0, len(FileSeq)):
            fWtxt.write(str(FileSeq[i]))
    fWtxt.close()
