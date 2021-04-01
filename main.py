import os, sys
from pprint import pprint
import GaussianRunPack
				
usage ='Usage; %s infile' % sys.argv[0]

try:
    infilename = sys.argv[1]
except:
    print (usage); sys.exit()


#if len(sys.argv)==3: option = sys.argv[2]

#For reading log file ####
#option = "eae homolumo"
#test_sdf = GaussianRunPack.GaussianDFTRun('B3LYP', 'STO-3G', 12, option,infilename,0)
#outdic = test_sdf.Extract_values(infilename,0,0,0,0,0,1,1,0,0,0,0)
#print (outdic)
#########################


#for stargint from gaussian calculation
#option = "opt deen nmr ipe eae homolumo dipole uv fluor"
option = "opt stable2o2 eae ipe" 
solvent = "2.05"
test_sdf = GaussianRunPack.GaussianDFTRun('B3LYP', 'STO-3G', 12, option, solvent, infilename, 0)

outdic = test_sdf.run_gaussian()

print (outdic)
#######################################
