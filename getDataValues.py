import sys
from createDatasets import *


class Point():
    def __init__(self, datasetDict, xPoint, yPoint):
        self.dataValues = {}        
        for key in datasetDict:
            self.dataValues[key] = datasetDict[key].getInterpolatedValue(xPoint, yPoint)[0][0]
        # millimeters -> meters then water-equivalent to ice-equivalent
        self.dataValues['smb'] = self.dataValues['smb'] * (1.0 / 1000.0) * (916.7 / 1000.0)

def main(argv):
    myDictionary = createInitialDatasets()
    myPoint = Point(myDictionary, -98998.55768989387, -2159531.8275367804)
    print myPoint.dataValues    

if __name__ == '__main__':
    main(sys.argv)
