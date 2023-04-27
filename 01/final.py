id=""
myDictionary = []
def studentDictFromFile():
    global myDictionary
    global id
    f = open("ct.txt")
    id = f.read(9)
    a = f.read()
    f.close()
    quizzes = 0
    quizzesList = []
    assignments = 0
    assignmentsList = []
    assignmentsx = 0
    assignmentsxList = []
    k = ""
    while quizzes < 10:
        s = 0
        for x in range(1, len(a)):
            if a[x] != ";":
                k += a[x]
            elif a[x] == ";":
                quizzesList.append(int(k))
                quizzes += 1
                k = ""
                if quizzes == 10:
                    break
            s += 1
    while assignments < 8:
        t = 0
        for x in range(2 + s, len(a)):
            if a[x] != ";":
                k += a[x]
            elif a[x] == ";":
                assignmentsList.append(int(k))
                assignments += 1
                k = ""
                if assignments == 8:
                    break
            t += 1
    while assignmentsx < 5:
        for x in range(s + t + 3, len(a) - 1):
            if a[x] != ";":
                k += a[x]
            elif a[x] == ";":
                assignmentsxList.append(int(k))
                assignmentsx += 1
                k = ""
                if assignmentsx == 5:
                    break
    myDictionary={id:[quizzesList,assignmentsList,assignmentsxList]}
def calculateAverageGrades(inputDictionary):
    global id
    for x in inputDictionary:
        inputDictionary[x][0].sort()
        totalAssignments=inputDictionary[x][1]+inputDictionary[x][2]
        totalAssignments.sort()
        avQ=sum(inputDictionary[x][0][-8:])/len(inputDictionary[x][0][-8:])
        avA=sum(totalAssignments[-8:])/len(totalAssignments[-8:])
        print("Student ID:", id, "Average Quiz Grade:", avQ)
        print("Student ID:", id, "Average Assignment Grade:", avA)
studentDictFromFile()
calculateAverageGrades(myDictionary)
