from random import shuffle, randint

class doors:
    def __init__(self):
        self.doorValues = [True, False, False]
        shuffle(self.doorValues)

    def revealDoor(self, guess):
        for index,correct in enumerate(self.doorValues):
            if index!=guess and correct==False:
                return i

    def isCorrect(self, guess):
        return self.doorValues[guess]

    def resetDoors(self):
        shuffle(self.doorValues)

def printPercentages(totalStayWin, totalSwapWin):
    total = totalStayWin+totalSwapWin
    print("Percentage won having stayed: {}%".format(round(totalStayWin/total,2)))
    print("Percentage won having swapped: {}%".format(round(y/totalSwapWin,2)))

d = doors()
noTrials = 100
totalSwapWin, totalStayWin = 0, 0

for i in range(noTrials):
    initialGuess = randint(0,2)
    incorrectDoor = d.revealDoor(initialGuess)
    if d.isCorrect(initialGuess): #Don't switch to the other door
        totalStayWin += 1
    else: #Switch to the other door
        totalSwapWin += 1
    d.resetDoors()
printPercentages(totalStayWin, totalSwapWin)
