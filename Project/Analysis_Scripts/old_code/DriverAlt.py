import math as mt
import sys

#compare 2 files, if they are different, pass to data comparison (done)
def compareTo(inpFile1, inpFile2):
    if (inpFile1 < inpFile2):
        return -1
    elif (inpFile1 > inpFile2):
        return 1
    else:
        return 0

#create 2 arrays of file states
def states_to_arr(file1, file2):
    fileArr1 = list()
    fileArr2 = list()
    inpFile1 = open("/Users/jeffmills/PycharmProjects/EfficientKL_V1.0/LinuxAttackDataSet/" + file1, "r")
    inpFile2 = open("/Users/jeffmills/PycharmProjects/EfficientKL_V1.0/LinuxAttackDataSet/" + file2, "r")
    #inpFile1 = open("/home/millsjw2/GhoshMillsWork2/BatchKL/DataFiles2/" + file1, "r")
    #inpFile2 = open("/home/millsjw2/GhoshMillsWork2/BatchKL/DataFiles2/" + file2, "r")
    for line in inpFile1:
        words = line.split()
        for word in words:
            #print("state1: "+word)
            word = str(word)
            fileArr1.append(str(word))
    for line in inpFile2:
        words2 = line.split()
        for word in words2:
            word = str(word)
            fileArr2.append(word)

    #array containing all possible trans from the union of all states in both files (done) returns arr[x**2]
    allTransArr = stArr_union(fileArr1, fileArr2)

    #arrays containing the transitions in each file (done)
    file_trans1 = create_file_trans(fileArr1)
    file_trans2 = create_file_trans(fileArr2)

    #arrays that contain the number of times a transition occurs in each file (done) returns arr[x**2]
    trans_counts_file1 = get_counts(allTransArr, file_trans1)
    trans_counts_file2 = get_counts(allTransArr, file_trans2)

    #arrays that contain the total number of transitions away from a reference state (done) returns arr[x**2]
    file1_first_totals = get_first_total(allTransArr, fileArr1)
    file2_first_totals = get_first_total(allTransArr, fileArr2)

    #arrays that contain the probabilities of each transition in a file. Probs are related to allTransArr (done)
    file1_probs = get_probabilities(allTransArr, trans_counts_file1, file1_first_totals)
    file2_probs = get_probabilities(allTransArr, trans_counts_file2, file2_first_totals)

    KL1 = get_KL(file1_probs, file2_probs)
    KL2 = get_KL(file2_probs, file1_probs)
    JSD = get_JSD(file1_probs, file2_probs)

    return KL1, KL2, JSD

#create union of the states of the 2 files (done)
def stArr_union(fileArr1, fileArr2):
    union_Arr = list(set(fileArr1) | set(fileArr2))
    #for state in union_Arr:
      #  print("state: "+ state)
    trans_arr = create_all_trans(union_Arr)
    return trans_arr

#create all transitions from the union of the file states (done)
def create_all_trans(inpUnionArr):
    trans_arr = list()
    for state1 in inpUnionArr:
        for state2 in inpUnionArr:
            trans = str(state1 + " " + state2)
            trans_arr.append(trans)
    #for trans in trans_arr:
     #   print("trans: "+ trans)
    return trans_arr

#create 2 arrays that stores the transitions that occur in each file (done)
def create_file_trans(fileArr1):
    file1_trans = list()
    for i in range(0, len(fileArr1)-1):
        trans1 = fileArr1[i] + " " + fileArr1[i+1]
        file1_trans.append(trans1)
    return file1_trans

#return the counts for all of the possible transitions(assume each trans occurs min of 1 time) (done)
def get_counts(refArr, fileArr):
    trans_counts = list()
    for i in range(0, len(refArr)):
        ref_state = refArr[i]
        count = 1 ##
        for j in range(0,len(fileArr)):
            if (fileArr[j] == ref_state):
                count = count + 1
        trans_counts.append(count)
    #print("len: "+ str(len(trans_counts)))
    #print("TRANS COUNTS:" +str(trans_counts))
    return trans_counts

#create 2 arrays that contain the total number of transitions away from the first state in each
# transition(count each state, disregard last index) (done)
def get_first_total(refArr, fileArr):
    first_totals = list()
    for i in range(0, len(refArr)):
        st_arr = refArr[i].split()
        first_state = st_arr[0]
        count = 1 ##
        for j in range(0, (len(fileArr))-1):
            if fileArr[j] == first_state:
                count = count + 1
        first_totals.append(count)
    ##print("Firsts: "+str(first_totals))
    return first_totals

#create array that store probabilities associated with transitions (done)
def get_probabilities(refArr, numArr, denomArr):
    prob_arr = list()
    if(len(numArr) != len(denomArr)):
        print("WRONG!")
    for i in range(0,len(denomArr)):
        if(denomArr[i] == 0):
            prob = float(0)
        else:
            prob = (float(numArr[i])/ float(denomArr[i]))
        #print("TRANS: "+ refArr[i] + " NUM: "+ str(numArr[i]) +" DENOM: "+ str(denomArr[i]) + " prob: "+str(prob))
        prob_arr.append(prob)
    return prob_arr

#calculate KL (done)
def get_KL(file1_probs, file2_probs):
    if len(file1_probs) != len(file2_probs):
        print("WRONG KL Parameters!")
    sub_list = list()
    for i in range(0, len(file1_probs)):
        if(file2_probs[i] == 0.0 or file1_probs[i] == 0.0 or file2_probs[i] == 1.0 or file1_probs[i]== 1.0):
            kl_tot = 0.0
        elif(file2_probs[i]/file1_probs[i] == 1.0):
            kl_tot = 0.0
        elif(file1_probs[i]/file2_probs[i] == 1.0):
            kl_tot = 0.0
        else:
            ##print("f1p: "+str(file1_probs[i]) + " f2p: "+str(file2_probs[i]))
            kl_sub1 = file1_probs[i] * (mt.log10((file1_probs[i]/file2_probs[i])))
            kl_sub2 = (1-(file1_probs[i])) * (mt.log10(((1-file1_probs[i])/(1-file2_probs[i]))))
            kl_tot = kl_sub1 + kl_sub2
        sub_list.append(kl_tot)
    #print("KL_LIST: "+ str(sub_list))
    KL = sum(sub_list)
    return KL

#calculate JSD (done)
def get_JSD(file1_probs, file2_probs):
    M = list()
    for i in range(0, len(file1_probs)):
        m = 0.5*(file1_probs[i] + file2_probs[i])
        M.append(m)
    JSD = (0.5*(get_KL(file1_probs, M))) + (0.5*(get_KL(file2_probs, M)))
    return JSD


##MAIN METHOD
#inp = int(sys.argv[1])
#LenP = int(inp * 25)
LenQ = 748


OutKLMatrix = [[0 for x in range(LenQ+1)] for y in range(LenQ+1)]
OutJSDMatrix = [[0 for x in range(LenQ+1)] for y in range(LenQ+1)]

#OutputCSV = "/home/millsjw2/GhoshMillsWork2/BatchKL/OutputKL_"+str(LenP)+".csv"
#OutputJSD = "/home/millsjw2/GhoshMillsWork2/BatchKL/OutputJSD_"+str(LenP)+".csv"

for i in range(725, LenQ+1):
    for j in range(0, LenQ+1):
        if (j > i):
            File1 = "Trace"+str(i)+".txt"
            File2 = "Trace"+str(j)+".txt"
            KL1, KL2, JSD = states_to_arr(File1, File2) #submits 2 files, returns values
            #print("KL: "+ str(KL1) + "JSD: "+str(JSD))

            OutKLMatrix[i][j] = KL1
            OutKLMatrix[j][i] = KL2
            OutJSDMatrix[i][j] = JSD
            OutJSDMatrix[j][i] = JSD
            print("File1complete: "+ str(i)+ " File2complete: "+str(j))


#write a method to store information as CSV
#OutputCSV = "/home/millsjw2/GhoshMillsWork2/BatchKL/OutputKL3_"+str(LenQ+1)+".csv"
OutputCSV = "OutputKL3_749.csv"
with open(OutputCSV, "w") as out:
    for i in range(0,   LenQ+1):
        for j in range(0, LenQ + 1):
            out.write(str(OutKLMatrix[i][j])+",")
        out.write("\n")
out.close()

#OutputJSD = "/home/millsjw2/GhoshMillsWork2/BatchKL/OutputJSD3_"+str(LenQ+1)+".csv"
OutputJSD = "OutputJSD3_749.csv"
with open(OutputJSD, "w") as out:
    for i in range(0, LenQ + 1):
        for j in range(0, LenQ + 1):
            out.write(str(OutJSDMatrix[i][j])+",")
        out.write("\n")
out.close()