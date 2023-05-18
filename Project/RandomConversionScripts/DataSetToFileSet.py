import math as mt
import os

inputFile = open("/Users/jeffmills/PycharmProjects/EfficientKL_V1.0/malware_dataset/malware_API_dataset.csv", "r")

FileArray = list()
fileCount = 0

for line in inputFile:
    fileCount +=1
    FileSeq = list()
    word = ""
    for char in line:
        if char == ",":
            FileSeq.append(word)
            word = ""

        elif char != '"':
            word += char
    FileSeq.append(word)
    FileArray.append(FileSeq)

for i in range(0, len(FileArray)):
    outputTxt = "/Users/jeffmills/PycharmProjects/EfficientKL_V1.0/malware_dataset/TXTConvert/Trace"+ str(i) +".txt"
    with open(outputTxt, "w") as fWtxt:
        for j in range(2,len(FileArray[i])):
            fWtxt.write(FileArray[i][j] + " ")
    fWtxt.close()
