import os, sys 
import gc
import subprocess


def exe_Gaussian(jobname):

    GaussianResult = subprocess.run(["g16", jobname])
    #For shell=True############################################
    #cmd = "g16"+" " + PreGauInput[0]
    #GaussianResult = subprocess.run(cmd, shell=True)
    ##########################################################
    print (GaussianResult)
    del GaussianResult
    gc.collect()
