import random
records = open("records.txt", "r")
filteredData = open("filteredData.csv", "w+")
subjectDescription = open("subject-description.txt", "r")
labels = []

subjects = records.read()
subjects = subjects.split("\n")

subjectData = subjectDescription.read()
subjectData = subjectData.split("\n")

individualSubject = {}

for i in range(1, len(subjectData)):
    subjectData[i] = subjectData[i].split("\t")

for i in range(1, len(subjectData)):
    individualSubject[subjectData[i][0]] = subjectData[i][2:]

print(individualSubject)

for k in range(0, len(subjects)):
    fileName = subjects[k] + ".ts"
    f = open(fileName, "r")

    trapSummation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    data = f.read()
    data = data.split("\n")
    data = data[:-1]

    for i in range(0, len(data)):
        data[i] = data[i].split("\t")

    for i in range(0, len(data) - 1):
        for j in range(1, len(data[i])):
            trapSummation[j] = trapSummation[j] + (float(data[i + 1][0]) - float(data[i][0])) * \
                               (float(data[i][j]) + float(data[i + 1][j]))

    for i in range(0, len(trapSummation)):
        trapSummation[i] = (trapSummation[i] / 2) / (float(data[-1][0]) - float(data[0][0]))

    for i in range(1, len(trapSummation)):
        if i == 5 or i == 6 or i == 9 or i == 10 or i == 12:
            filteredData.write(str(trapSummation[i] / 100) + ",")
        else:
            filteredData.write(str(trapSummation[i]) + ",")

    for i in range(0, len(individualSubject[subjects[k]])):
        if i == 3:
            if individualSubject[subjects[k]][i] == "m":
                individualSubject[subjects[k]][i] = "1"
            elif individualSubject[subjects[k]][i] == "f":
                individualSubject[subjects[k]][i] = "0"
        if i == 5 and float(individualSubject[subjects[k]][i]) > 0:
            individualSubject[subjects[k]][i] = "1"
            filteredData.write(individualSubject[subjects[k]][i])
            labels.append(individualSubject[subjects[k]][i])
        elif i == 5 and float(individualSubject[subjects[k]][i]) == 0:
            filteredData.write(individualSubject[subjects[k]][i])
            labels.append(individualSubject[subjects[k]][i])
        else:
            filteredData.write(individualSubject[subjects[k]][i] + ",")

    filteredData.write("\n")

options = [0, 1]
randomControl = []
for i in range(0, len(labels)):
    randomControl.append(random.choice(options))

controlAcc = 0
for i in range(0, len(labels)):
    if int(labels[i]) == int(randomControl[i]):
        controlAcc = controlAcc + 1

print(labels)
print(randomControl)

print(controlAcc / len(labels))