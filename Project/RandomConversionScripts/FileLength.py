Community1 = [12, 29, 43, 55, 56, 94, 134, 219, 222, 239, 262, 263, 265, 308, 347]
Community2 = [17, 93, 147, 168, 213, 236, 321, 372, 374] #125 but its very long
Community3 = [3, 11, 15, 52, 82, 149, 268, 314, 353, 367]
Community4 = [16, 20, 39, 107, 128, 203, 226, 233, 254, 277, 287, 291, 373]
## Community5 = [9, 22, 54, 62, 64, 81, 89, 90, 99, 164, 252, 309] All Files Are Long
Community6 = [88, 98, 127, 162 , 249, 275, 280, 327, 364] #105 but its very long
Community7 = [4, 26, 58, 69, 103, 109, 142, 156, 157, 170, 201, 209, 243, 302, 306, 311, 370, 371]
Community8 = [38, 49, 79, 85, 87, 106, 114, 115, 117, 122, 132, 153, 154, 179, 197, 234, 257, 286, 305]


for i in range(0,len(Community7)):
    File1 = "Trace" + str(Community7[i]) + ".txt"
    Name1 = str(Community7[i])
    for j in range(0,len(Community7)):
        Name2 = str(Community7[j])
        if (j != i) and (j < i) :
            File2 = "Trace" + str(Community7[j]) + ".txt"

            inpFile1 = open("/Users/jeffmills/CIT277_millsjw2/MalwareDataCollector/DataFiles/" + File1, "r")
            inpFile2 = open("/Users/jeffmills/CIT277_millsjw2/MalwareDataCollector/DataFiles/" + File2, "r")
            Str1 = list()
            Str2 = list()
            for line in inpFile1:
                words = line.split()
                for word in words:
                    Str1.append(word)
            for line in inpFile2:
                words2 = line.split()
                for word in words2:
                    Str2.append(word)

            print("FILE1: "+ Name1 + " LEN: "+ str(len(Str1))+" FILE2: "+ Name2+ " LEN: "+str(len(Str2)))

for i in range(0,len(Community8)):
    File1 = "Trace" + str(Community8[i]) + ".txt"
    Name1 = str(Community8[i])
    for j in range(0,len(Community8)):
        Name2 = str(Community8[j])
        if (j != i) and (j < i) :
            File2 = "Trace" + str(Community8[j]) + ".txt"

            inpFile1 = open("/Users/jeffmills/CIT277_millsjw2/MalwareDataCollector/DataFiles/" + File1, "r")
            inpFile2 = open("/Users/jeffmills/CIT277_millsjw2/MalwareDataCollector/DataFiles/" + File2, "r")
            Str1 = list()
            Str2 = list()
            for line in inpFile1:
                words = line.split()
                for word in words:
                    Str1.append(word)
            for line in inpFile2:
                words2 = line.split()
                for word in words2:
                    Str2.append(word)


            print("FILE1: " + Name1 + " LEN: " + str(len(Str1)) + " FILE2: " + Name2 + " LEN: " + str(len(Str2)))

for i in range(0,len(Community6)):
    File1 = "Trace" + str(Community6[i]) + ".txt"
    Name1 = str(Community6[i])
    for j in range(0,len(Community6)):
        Name2 = str(Community6[j])
        if (j != i) and (j < i) :
            File2 = "Trace" + str(Community6[j]) + ".txt"

            inpFile1 = open("/Users/jeffmills/CIT277_millsjw2/MalwareDataCollector/DataFiles/" + File1, "r")
            inpFile2 = open("/Users/jeffmills/CIT277_millsjw2/MalwareDataCollector/DataFiles/" + File2, "r")
            Str1 = list()
            Str2 = list()
            for line in inpFile1:
                words = line.split()
                for word in words:
                    Str1.append(word)
            for line in inpFile2:
                words2 = line.split()
                for word in words2:
                    Str2.append(word)

            print("FILE1: " + Name1 + " LEN: " + str(len(Str1)) + " FILE2: " + Name2 + " LEN: " + str(len(Str2)))