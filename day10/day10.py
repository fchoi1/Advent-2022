
class Tube():
    
    def getInput(self):
        file1 = open('input.txt', 'r')
        #file1 = open('input-test.txt', 'r')
        Lines = file1.readlines()
        data = []
        # Get input data
        for line in Lines:
            data.append(line.strip())
        return data

    def __init__(self) -> None:
        """ Main entry point of the app """
        self.inputData = self.getInput()
        self.cycle = 0
        self.value = 1
        self.signalStrengths = [20, 60, 100, 140, 180, 220]
        self.totalSum = 0
        self.CRTrow = 6
        self.CRTpixel = 40
        self.CRT = [['.'] * self.CRTpixel for i in range(self.CRTrow)] 
    def runProgram(self):
        for row in self.inputData:
            commandArr = row.split(' ')
            self.updateCRT()
            self.cycle += 1
            self.checkSignalStrength(commandArr)

            if commandArr[0] == 'addx':
                self.updateCRT()
                self.cycle += 1
                self.checkSignalStrength(commandArr)
                self.value += int(row.split(' ')[1])

    def checkSignalStrength(self, command: list[str] = []):
        if self.cycle in self.signalStrengths:
            strength = self.signalStrengths.pop(self.signalStrengths.index(self.cycle))
            self.totalSum += self.value * strength
    
    def updateCRT(self):
        self.currRow = self.cycle // 40
        self.currCol = self.cycle % 40
        if self.value-1 <= self.cycle%40 <= self.value + 1:
            self.CRT[self.currRow][self.currCol] = '#'

    def getTotalSum(self):
        return self.totalSum
    
    def getCRT(self):
        for row in self.CRT:
            print('  '.join(row))
        pass

if __name__ == "__main__":
    """ This isexecuted when run from the command line """
    tube = Tube()
    tube.runProgram()
    print('Day 10 part 1:', tube.getTotalSum())
    print('Day 10 part 2:', tube.getCRT())
