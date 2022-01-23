import csv

undeliveredFile = open("C:\\Users\\pulig\\PycharmProjects\\removeUndelivered\\undelivered.txt", "r")
sentToDict = {}
uniqDict = {}
sentToFile = open("C:\\Users\\pulig\\PycharmProjects\\removeUndelivered\\sentToFinal.csv")

lines = undeliveredFile.read()
undeliveredList = lines.splitlines()

undeliveredFile.close()

# print(undeliveredList)


for line in sentToFile:
    key, value = line.split(",")
    sentToDict[key] = value.rstrip("\n")

# for sentToDict[key] in undeliveredList:
#   removedValue = sentToDict.pop(key)
#   print(removedValue)


new_dict = {key: val for key, val in sentToDict.items() if val not in undeliveredList}

print(new_dict)

with open('C:\\Users\\pulig\\PycharmProjects\\removeUndelivered\\finalListSent.csv', 'w') as f:
    for key in new_dict.keys():
        f.write("%s,%s\n"%(key,new_dict[key]))
