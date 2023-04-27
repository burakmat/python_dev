def nameComparitor(inputString1, inputString2):
    wordCount=0
    if inputString1!="" and inputString2!="":
        if inputString1[0]>inputString2[0]:
            wordCount+=1
            return wordCount+nameComparitor(inputString1.replace(inputString1[0],""),inputString2.replace(inputString2[0],""))
        elif inputString1[0]==inputString2[0]:
            wordCount+=5
            return wordCount + nameComparitor(inputString1.replace(inputString1[0], ""),
                                              inputString2.replace(inputString2[0], ""))
        elif inputString1[0]<inputString2[0]:
            wordCount-=1
            return wordCount + nameComparitor(inputString1.replace(inputString1[0], ""),
                                              inputString2.replace(inputString2[0], ""))
    elif (inputString1==""and inputString2!="") or (inputString2=="" and inputString1!=""):
        return wordCount
    elif inputString1=="" and inputString2=="":
        return wordCount

print("Name is : Burak Mat ","| Name comparision result is: ",nameComparitor("Burak","Mat"))