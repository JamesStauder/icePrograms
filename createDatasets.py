import time
import h5py
import numpy as np
import sys
from pylab import sqrt, linspace
from scipy.interpolate import RectBivariateSpline


dataFileName = 'data/GreenlandInBedCoord_V2.h5'
dataMap = {'x0': 0, 'y0': 0,  'x1': 10018, 'y1': 17946,
       'cmap_x0': 0, 'cmap_y0': 0,
       'cmap_x1': 10018, 'cmap_y1': 17946,
       'proj_x0': -637925, 'proj_x1': 864625,
       'proj_y0': -657675, 'proj_y1': -3349425,
       'cmap_proj_x0': -637925, 'cmap_proj_x1': 864625,
       'cmap_proj_y0': -657675, 'cmap_proj_y1': -3349425}

def createInitialDatasets():
    print "Creating data sets"
    t0 = time.time()

    datasetDict = {}

    dataFile = h5py.File(dataFileName, 'r')
    dataMap['x1'] = len(dataFile['bed'][:][0])
    dataMap['y1'] = len(dataFile['bed'][:])
    dataMap['proj_x1'] = dataFile['x'][:][-1]
    dataMap['proj_y1'] = dataFile['y'][:][-1]
    velocity = Dataset('velocity')
    datasetDict['velocity'] = velocity

    smb = Dataset('smb')
    datasetDict['smb'] = smb

    bed = Dataset('bed')
    datasetDict['bed'] = bed

    surface = Dataset('surface')
    datasetDict['surface'] = surface

    thickness = Dataset('thickness')
    datasetDict['thickness'] = thickness

    t2m = Dataset('t2m')
    datasetDict['t2m'] = t2m

    datasetDict['VX'] = Dataset('VX')
    datasetDict['VY'] = Dataset('VY')

    dataFile.close()

    print "Loaded all data sets in ", time.time() - t0, " seconds"
    return datasetDict


class Dataset:
    def __init__(self, name):
        self.name = name

        bed_xarray = linspace(dataMap['proj_x0'], dataMap['proj_x1'], dataMap['x1'], endpoint=True)
        bed_yarray = linspace(dataMap['proj_y1'], dataMap['proj_y0'], dataMap['y1'], endpoint=True)

        if self.name == 'velocity':
            self.data = self.setData(name)
        else:
            self.data = self.setData(name)

        self.interp = RectBivariateSpline(bed_xarray, bed_yarray, np.flipud(self.data).transpose())


    def setData(self, name):
        dataFile = h5py.File(dataFileName, 'r')
        if name == 'velocity':
            vx = dataFile['VX'][:]
            vy = dataFile['VY'][:]
            data = sqrt(vx ** 2 + vy ** 2)
            dataFile.close()
            return data
        else:
            data = dataFile[name][:]
            dataFile.close()
            return data

    def getInterpolatedValue(self, xPosition, yPosition):
        return self.interp(xPosition, yPosition)



def main(argv):
    myDataset = createInitialDatasets()
    print myDataset['velocity']


if __name__ == '__main__':
    main(sys.argv)
