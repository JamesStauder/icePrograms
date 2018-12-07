import sys
from support.FlowIntegrator import *
from getDataValues import *
from scipy.interpolate import interp1d


class Profile():
    def __init__(self, datasetDict, shear1, shear2, dataFileName, average):

        t2m = []
        surface = []
        thickness = []
        bed = []
        velocity = []
        VX = []
        VY = []
        smb = []
        
        if average:

                
        else:

            midFlowline = []
            for i in range(0, len(shear1):
                midFlowline.append(None)
            midFlowline[0] = [(shear1.flowLine[0] + shear2.flowLine[0])/2, (shear1.flowLine[1] + shear2.flowLine[1])/2)]
            myIntegrator = FlowIntegrator(datasetDict['VX'], datasetDict['VY'],)
            midFlowline = myIntegrator.integrate(midFlowline[0][0], midFlowline[0][1], midFlowline, 0, 1000)
            if None in midFlowline:
                print "Integration Error Try Again"
    

            for point in midFlowline:
                myPoint = Point(datasetDict, point[0], point[1])
                t2m.append(myPoint['t2m'])
                surface.append(myPoint['surface'])
                thickness.append(myPoint['thickness'])
                bed.append(myPoint['bed'])
                velocity.append(myPoint['velocity'])
                VX.append(myPoint['VX'])
                VY.append(myPoint['VY'])
                smb.append(myPoint['smb'])


        f = h5py.File(dataFileName, 'w')
        f.create_dataset("smb", data = np.asarray(smb))
        f.create_dataset("t2m", data = np.asarray(t2m))
        f.create_dataset("surface", data = np.asarray(surface))
        f.create_dataset("thickness", data = np.asarray(thickness))
        f.create_dataset("bed", data = np.asarray(bed))
        f.create_dataset("velocity", data = np.asarray(velocity))
        f.create_dataset("VX", data = np.asarray(VX))
        f.create_dataset("VY", data = np.asarray(VY))

        f.close()
        
def main(argv):




if __name__ == '__main__':
    main(sys.argv)
