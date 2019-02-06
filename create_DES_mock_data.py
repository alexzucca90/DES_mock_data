import numpy as np
import matplotlib.pyplot as plt
import pylab as pil

# Utilities Libraries
from argparse import ArgumentParser

## Setting up argument parser
parser = ArgumentParser(description='DES MG mock data generator', usage='python create_DES_mock_data.py -t theory -i inverse_covariance -o output')

parser.add_argument('-t', '--theory',  type = str, help='file containing the theory predictions')
parser.add_argument('-i', '--invcov',  type = str, help='file containing the inverse covariance matrix')
parser.add_argument('-o', '--output',  type = str, help='output_file')
parsed = parser.parse_args()

theory = parsed.theory
icov = parsed.invcov
output = parsed.output

# loading the data
xip = np.loadtxt('./data/DES_1YR_final_xip.dat')
xim = np.loadtxt('./data/DES_1YR_final_xim.dat')
gammat = np.loadtxt('./data/DES_1YR_final_gammat.dat')
wtheta = np.loadtxt('./data/DES_1YR_final_wtheta.dat')

# these are the items used for the final 1YR DES analysis
used_items = np.loadtxt('./data/DES_used_items.dat')

# loading the MG theoretical predictions
mg = np.loadtxt(theory)

# load the covariance matrix
invcov = np.loadtxt(icov)

#invert the covariance matrices
cov = np.linalg.inv(invcov)

# generate the mock data
mock = np.random.multivariate_normal(mg, cov)

# now start modifying the data
for meas_type in range(1,5):
    # just create the array of mock data
    if meas_type == 1:
        this_mock = xip.copy()
        outname = './output/DES_mock_data_'+output+'_xip.dat'
    elif meas_type == 2:
        this_mock = xim.copy()
        outname = './output/DES_mock_data_'+output+'_xim.dat'
    elif meas_type == 3:
        this_mock = gammat.copy()
        outname = './output/DES_mock_data_'+output+'_gammat.dat'
    elif meas_type == 4:
        this_mock = wtheta.copy()
        outname = './output/DES_mock_data_'+output+'_wtheta.dat'
        
    for b1 in range(1,6):
        for b2 in range(1,6):
            #print('meas, b1, b2:', meas_type, b1, b2)
            # select the data for this measurement, and bins
            this_items = np.where((used_items[:,0] == meas_type)&(used_items[:,1] == b1)&(used_items[:,2] == b2))
            
            # and check the angle bins
            theta_bins_used = used_items[this_items]
            
            # select the mock data for these bins
            this_data = mock[this_items]
            
            if theta_bins_used.shape[0] > 0:
                for i in range(theta_bins_used.shape[0]):
                    #print('i:',i)
                    for j in range(this_mock.shape[0]):
                        #print('j:',j)
                        if (this_mock[j,0] == b1 and this_mock[j,1] == b2 and this_mock[j,2] == theta_bins_used[i,3]):
                            this_mock[j,3] = this_data[i]

    
    # here I should save the mock data
    file = open(outname, 'w')
    file.write('# BIN1 BIN2 ANGBIN VALUE \n')
    for n in range(this_mock.shape[0]):
        file.write(str(int(this_mock[n,0]))+' '+str(int(this_mock[n,1]))+' '+str(int(this_mock[n,2]))+' '+str(this_mock[n,3])+'\n')
    file.close()
