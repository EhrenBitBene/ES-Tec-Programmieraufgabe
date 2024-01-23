import time
import csv
import random
import os 

def rekursiv(biggestMat,smallestMat,step,matCount=0):
    startTime = time.time()
    if biggestMat >= smallestMat:
         rekursiv(biggestMat - step,smallestMat,step,matCount + 1)
    
    endTime = time.time()    
    return [matCount,endTime - startTime]
    
    


def iterativ(biggestMat,smallestMat,step,matCount=0):
    startTime = time.time() 
    while biggestMat >= smallestMat:
        biggestMat -= step
        matCount += 1
    
    endTime = time.time()

    return [matCount,endTime - startTime]

def manualOutput():    
    
    biggestMat = int(input("Wie groß ist \n die Größte Matroschka: "))
    smallestMat = int(input("Wie klein ist \n die Kleinste Matroschka: "))
    stepSize = int(input("Wie viel Prozent soll \n die nächste Matroschka kleiner sein: "))
    chooseLoop = input("Wähle die art der Schleife: ")
    step = biggestMat * (stepSize/100)

    if chooseLoop.lower() == "ri":
        rekursivOutput = rekursiv(biggestMat,smallestMat,step)
        print("Zeit:" + str(round(rekursivOutput[1]*1000, 7)))
        print(str(rekursivOutput[0]) + " Matroschkas passen zwischen die größte und kleinste")

    elif chooseLoop.lower() == "iterativ":
        iterativOutput = iterativ(biggestMat,smallestMat,step)
        print("Zeit:" + str(round(*1000, 7)))
        print(str(iterativOutput[0]) + " Matroschkas passen zwischen die größte und kleinste")

def randomOut():
    randomAttemptsOutputarray = [None] * randomAttempts
    for i in range(randomAttempts):
        biggestMat = random.randint(1,1000)
        smallestMat = random.randint(1,biggestMat-1)
        stepSize = random.randint(1,100)
        step = biggestMat * (stepSize/100)
        
        rekursivOutput = rekursiv(biggestMat,smallestMat,step) 

        iterativOutput = iterativ(biggestMat,smallestMat,step) 

        randomAttemptsOutputarray[i] = [biggestMat,smallestMat,int(round(step, 0)),rekursivOutput,iterativOutput]

    with open("MatFeldversuch.csv",mode="w",newline="") as file:
        writer = csv.writer(file, delimiter=';') # delimiter = ';' sorgt dafür das , als zeichen für eine neue zelle erkannt wird
        writer.writerow(["Größte Matroschka", "Kleinste Matroschka", "Schrittgröße", "Anzahl Matroschkas", "Rekursiv Zeit", "Iterativ Zeit"])
        
            
        for i in range(randomAttempts):
            writer.writerow([randomAttemptsOutputarray[i][0], randomAttemptsOutputarray[i][1], randomAttemptsOutputarray[i][2], randomAttemptsOutputarray[i][4][0], str(round(randomAttemptsOutputarray[i][3][1], 7)) + "ms", str(round(randomAttemptsOutputarray[i][4][1], 7)) + "ms"])    
        
    os.startfile("MatFeldversuch.csv")
    
inputType = input("manuelle oder zufällige Eingabe?")

if inputType.lower() == "manuell":
    manualOutput()

elif inputType.lower() == "zufällig":
    randomAttempts = int(input("Wie viele Zufallsversuche:"))
    randomOut()
     
