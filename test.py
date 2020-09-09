set1 = set((1,2,3,4,5,6,7,8,9,10))
set2 = set((1,2,3,4,5,6,7,8,9,10))
set3 = set((2,3,4,5,6,7,8,9,10,11))
set4 = set((5,6,7,8,9,10,11,12,13,14))
listOfSets = [set1, set2, set3, set4]

def distance(set1, set2):
    return float(len(set1.symmetric_difference(set2)))/float(len(set1.union(set2)))

for left in listOfSets:
    for right in listOfSets:
        print distance(left, right)

