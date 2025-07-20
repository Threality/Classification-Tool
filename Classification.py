import pandas as pd
import math
import time
import numpy

def CreateDecisionTree(data, maxDepth):
    class Tree:
        def __init__(self):
            nodes = 0

    class Node:
        def __init__(self):
            pass

    def CreateLeaf(data, maxDepth, curDepth, prevNode):
        columns = data.columns
        finalName = data.columns[len(columns) - 1]
        bestSolutions = []
        for i in range(len(columns) - 1):
            curVals = data[columns[i]]
            if isinstance(curVals[0], numpy.int64) or isinstance(curVals[0], float):
                print(f'{curVals[0]}: numeric')
                bestSolutions.append(FindNumericMax(curVals, data, finalName, columns[i]), columns[i])
            else:
                print(f'{curVals[0]}: categorical')
        print(bestSolutions)

    def FindNumericMax(vals, data, finalName, curName):
        minVal = min(vals)
        step = (max(vals) - minVal) / 1000
        minEntropy = float('inf')
        for i in range(1000):
            curEntropy = GetEntropy(minVal + (i * step), data, finalName, curName)
            if curEntropy < minEntropy:
                minEntropy = curEntropy
                bestVal = minVal + (i * step)
        return minEntropy, bestVal

    def GetEntropy(keyVal, data, finalName, curName):
        if not(isinstance(data[(data.columns)[len(data.columns) - 1]][0], numpy.int64) or isinstance(data[(data.columns)[len(data.columns) - 1]][0], float)):
            outcomes = data[finalName].unique()
            lEntropy = 0
            for i in range(len(outcomes)):
                numerator = len(data[(data[curName] <= keyVal) & (data[finalName] == outcomes[i])])
                denominator = len(data[(data[curName] <= keyVal)])
                if numerator == 0:
                    continue
                if denominator == 0:
                    return float('inf')

                lEntropy -= (numerator / denominator) * math.log2(numerator / denominator)
            
            rEntropy = 0
            for i in range(len(outcomes)):
                numerator = len(data[(data[curName] > keyVal) & (data[finalName] == outcomes[i])])
                denominator = len(data[(data[curName] > keyVal)])
                if numerator == 0:
                    continue
                if denominator == 0:
                    return float('inf')

                rEntropy -= (numerator / denominator) * math.log2(numerator / denominator)

            totLeft = len(data[data[curName] <= keyVal])
            totRight = len(data[data[curName] > keyVal])
            total = totLeft + totRight

            return (totLeft / total) * lEntropy + (totRight / total) * rEntropy

        else:
            print('Unable to perform on categorical currently')




    startTime = time.monotonic()
    print(f'\rCreating tree...', end='', flush=True)

    curTree = Tree()
    CreateLeaf(data, maxDepth, 1, curTree)

    print(f'\rTree created in {(time.monotonic() - startTime):.2f} seconds\n', end='', flush = True)

def ReadFile(filePath):
    startTime = time.monotonic()
    print(f'\rReading file...', end='', flush=True)
    data = pd.read_csv(filePath)
    print(f'\rRead file in {(time.monotonic() - startTime):.2f} seconds\n', end='', flush = True)
    return data

if __name__ == '__main__':
    data = ReadFile("weather_classification_data.csv")
    trainingLimit = math.floor(0.8*len(data))
    CreateDecisionTree(data[:trainingLimit], maxDepth=1)