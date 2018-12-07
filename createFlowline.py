import sys
from support.FlowIntegrator import *

class Flowline():
    def __init__(self, xStart, yStart, datasetDict, distance):
        self.distance = distance
        myIntegrator = FlowIntegrator(datasetDict['VX'], datasetDict['VY'])
        
        self.flowLine = []
        for x in range(0, self.distance):
            self.flowLine.append(None)

        self.flowLine[0] = [xStart, yStart] 
        self.flowLine = myIntegrator.integrate(xStart, yStart, self.flowLine, 0, 1000)

        if (None in self.flowLine):
            print "Integration Error try again with new x, y"
        



def main(argv):
    latPoint = 69.87
    longPoint = -47.01

    from translation import *
    myTranslator = LonLatToProj([[longPoint, latPoint]])

    from createDatasets import *
    myDatasetDict = createInitialDatasets()    


    myFlowline = Flowline(myTranslator.xPoints[0], myTranslator.yPoints[0], myDatasetDict, 100)
    
    print myFlowline.flowLine


if __name__ == '__main__':
    main(sys.argv)
