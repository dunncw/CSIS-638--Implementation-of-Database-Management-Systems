import os

inputDir = "/Users/jeffmills/PycharmProjects/EfficientKL_V1.0/Attack_Data_Master"
index = 0

for (dirpath, dirnames, filesnames) in os.walk(inputDir):
    for dirname in dirnames:
        newDir = os.listdir("/Users/jeffmills/PycharmProjects/EfficientKL_V1.0/Attack_Data_Master/"+str(dirname))
        for file in newDir:
            FileSeq = list()
            if file.endswith('.txt'):
                # print("FileName: "+ file)
                inpFile = "/Users/jeffmills/PycharmProjects/EfficientKL_V1.0/Attack_Data_Master/"+str(dirname)+"/"+str(file)
                with open(inpFile, "r") as inp:
                    for line in inp:
                        for int in line:
                            FileSeq.append(str(int))

            outputTxt = "/Users/jeffmills/PycharmProjects/EfficientKL_V1.0/LinuxAttackDataSet/Trace" + str(index) + ".txt"
            index += 1
            with open(outputTxt, "w") as fWtxt:
                for i in range(0, len(FileSeq)):
                    fWtxt.write(str(FileSeq[i]))
            fWtxt.close()

