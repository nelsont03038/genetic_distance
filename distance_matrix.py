import math

#11A7 (10E9 parent, child to CHOK1SV)
inFile1 = 'C:/Users/nelsot10/Desktop/phylogenetics/snp/C8A.snp'
#RN6G P4E4 - high expressor SSI line
inFile2 = 'C:/Users/nelsot10/Desktop/phylogenetics/snp/C15A.snp'
#RN6G P9G7 - high expressor SSI line
inFile3 = 'C:/Users/nelsot10/Desktop/phylogenetics/snp/C16A.snp'
#RN6G P4B2 - low expressor SSI line
inFile4 = 'C:/Users/nelsot10/Desktop/phylogenetics/snp/C17A.snp'
#RN6G P5D8 - low expressor SSI line
inFile5 = 'C:/Users/nelsot10/Desktop/phylogenetics/snp/C18A.snp'
#RN6G P9G7 100 gen
inFile6 = 'C:/Users/nelsot10/Desktop/phylogenetics/snp/C33A.snp'
#144E12
inFile7 = 'C:/Users/nelsot10/Desktop/phylogenetics/snp/C6A.snp'
#87H1 (sibling to 144E12)
inFile8 = 'C:/Users/nelsot10/Desktop/phylogenetics/snp/C7A.snp'


f = open(inFile1, 'r')
C8A = []
for line in f.readlines():
    newLine = line.split('\t')
    C8A.append(newLine[0] + "_" + newLine[1]  + "_" + newLine[3]  + "_" + newLine[4])            
f.close()

f = open(inFile2, 'r')
C15A = []
for line in f.readlines():
    newLine = line.split('\t')
    C15A.append(newLine[0] + "_" + newLine[1]  + "_" + newLine[3]  + "_" + newLine[4])            
f.close()

f = open(inFile3, 'r')
C16A = []
for line in f.readlines():
    newLine = line.split('\t')
    C16A.append(newLine[0] + "_" + newLine[1]  + "_" + newLine[3]  + "_" + newLine[4])            
f.close()

f = open(inFile4, 'r')
C17A = []
for line in f.readlines():
    newLine = line.split('\t')
    C17A.append(newLine[0] + "_" + newLine[1]  + "_" + newLine[3]  + "_" + newLine[4])            
f.close()

f = open(inFile5, 'r')
C18A = []
for line in f.readlines():
    newLine = line.split('\t')
    C18A.append(newLine[0] + "_" + newLine[1]  + "_" + newLine[3]  + "_" + newLine[4])            
f.close()

f = open(inFile6, 'r')
C33A = []
for line in f.readlines():
    newLine = line.split('\t')
    C33A.append(newLine[0] + "_" + newLine[1]  + "_" + newLine[3]  + "_" + newLine[4])            
f.close()

f = open(inFile7, 'r')
C6A = []
for line in f.readlines():
    newLine = line.split('\t')
    C6A.append(newLine[0] + "_" + newLine[1]  + "_" + newLine[3]  + "_" + newLine[4])            
f.close()

f = open(inFile8, 'r')
C7A = []
for line in f.readlines():
    newLine = line.split('\t')
    C7A.append(newLine[0] + "_" + newLine[1]  + "_" + newLine[3]  + "_" + newLine[4])            
f.close()

a = set(C8A)
b = set(C15A)
c = set(C16A)
d = set(C17A)
e = set(C18A)
f = set(C33A)
g = set(C6A)
h = set(C7A)

listOfSets = [a,b,c,d,e,f,g,h]
genome_size = 2258263190

def distance(set1, set2):
#    pdistance = float(len(set1.symmetric_difference(set2)))/float(len(set1.union(set2)))
    pdistance = float(len(set1.symmetric_difference(set2)))/genome_size
    jc69 = ((-3/4)*(math.log(1-(4/3)*pdistance))) #Jukes and Cantor model
#    return pdistance
    return jc69

for left in listOfSets:
    for right in listOfSets:
        print(distance(left, right))


'''
C8	11A7 (parent to 10E9)
C15	RN6G P4E4	high expressor
C16	RN6G P9G7	high expressor
C17	RN6G P4B2 	low expressor
C18	RN6G P5D8	low expressor
C33	RN6G P9G7   100 gen
C6	GS KO-Pfizer (144E12)
C7	GSKO-Pfizer (87H1)
'''
