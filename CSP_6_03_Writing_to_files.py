import random

#You need to create your own test file for this assignment.
#Because we are dealing with both reading and writing to files. Your test file will be more complicated than it has been.

def example (x):
    print(x)


def writeFile(inputList, fileName): #filename = "InputWriting.txt"
    #Creates a file of the given name and adds each value from the list to said file with each line being an index from the list.
    file = open(fileName, "w")
    for i in range(len(inputList)):
        if i==len(inputList)-1:
            TheInput = f"{inputList[i]}"
        else:
            TheInput = f"{inputList[i]}\n"
        file.write(TheInput)
    return(fileName)


def sortNames(fileName, targetFile):
    #Modify the below function such that it takes in source file and a target file.
    #Sort all of the values from the source file and write them to the target file
    #I recommend using .sort() for this. You do not need to write the sorting algorithm yourself.
    f = open(fileName, "r")
    list = []
    TheInput = []
    for i in f:
        #i = fileName.readline(1)
        list.append(i)
    for i in range(len(list)):
        if i == len(list) -1:
            list[i] = f"{list[i]}" + "\n"
        else:
            continue
    list.sort()
    print(list)
    d = open(targetFile, "w")
    for i in range(len(list)-1):
        d.write(list[i])
    list[-1] = list[-1].strip()
    d.write(list[-1])
    return(targetFile)



sortNames("source.txt", "target.txt")




def highScore( newScore: int):
    #Modify the function such that it adds a new score to the file scores.txt
    #Then return the average score from all of the scores in scores.txt
    with open("scores.txt", "a") as file:
        file.write(str(newScore) + "\n")
    list = []
    with open("scores.txt", "r") as file:
        for line in file:
            list.append(int(line))
        x = sum(list)
        y = len(list)
        average = x/y
    return(int(average))

