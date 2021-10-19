import os, sys, math
import re, gc
from numpy import *
import GaussianRunPack.AtomInfo

def Make_xyzfile(atom, X, Y, Z, ofile, charge, spin):

    s = ""
    s += str(len(atom)) + "\n"
    s += str(charge)+" "+ str(spin)+"\n"

    ofile = open(ofile,'w')

    ofile.write(s)

    for i in range(len(atom)):
        ofile.write('%-4s % 10.5f % 10.5f % 10.5f \n' % (atom[i], X[i], Y[i], Z[i]))

    ofile.close()


def Extract_Coordinate(lines, outfile=None):

    print ("Start finding coordinates...")

    Atom_index = []
    NumElement = []
    AtomicType = []
    X = []
    Y = []
    Z = []

    count = 0
    count_Station = 0
    Total_NumStation =0
    Index_Station = 0

######Counting Stationary points##############
    for line in lines:
        if line.find("Charge =") >= 0:
            line_charge_spin = line.split()
            given_Charge = int(line_charge_spin[2]) 
            given_SpinMulti = int(line_charge_spin[-1])
        if line.find("-- Stationary point found.") >= 0:
            count_Station += 1
##############################################
    Total_NumStation = count_Station

    if Total_NumStation > 0:
        count_Station = 0
        print ("Total number of stationary points: ", Total_NumStation)
        for line in lines:
            if line.find("-- Stationary point found.") >= 0:
                count_Station += 1
                Index_Station += 1
                print ("A stationary point is found! #", Index_Station)
                continue
            if line.find("Standard orientation:") >=0 and count_Station > 0:
#                    print ("Standard orientaion was found")
#                    print ("Start reading coordinate")
                count += 1
                continue
            if count == 1:
                Border_1 = line
#                    print (Border_1)
                count += 1
                continue
            if count == 2:
                Index_1 = line
#                    print (Index_1)
                count += 1
                continue
            if count == 3:
                Index_2 = line
#                    print (Index_2)
                count += 1
                continue
            if count == 4:
                Border_2 = line
#                    print (Border_2)
                count += 1
                continue
            if count >= 5:
                i_atom = line.split()
#                    print (i_atom)
                if len(i_atom) == 6:
                    Atom_index.append(int(i_atom[0]))
                    NumElement.append(int(i_atom[1]))
                    AtomicType.append(int(i_atom[2]))
                    X.append(float(i_atom[3]))
                    Y.append(float(i_atom[4]))
                    Z.append(float(i_atom[5]))
                    count += 1
                    continue
                else :
                    print ("Reading atom coordinates is finished...")
                    N = count-5
                    print ("Number of atoms: ", N)
                    count = 0
                    count_Station = 0
                continue

    else:
        for line in lines:
            if line.find("Standard orientation:") >=0:
                print ("Standard orientaion was found")
                print ("Start reading coordinate")
                count += 1
                continue
            if count == 1:
                Border_1 = line
#                    print (Border_1)
                count += 1
                continue
            if count == 2:
                Index_1 = line
#                    print (Index_1)
                count += 1
                continue
            if count == 3:
                Index_2 = line
#                    print (Index_2)
                count += 1
                continue
            if count == 4:
                Border_2 = line
#                    print (Border_2)
                count += 1
                continue
            if count >= 5:
                i_atom = line.split()
#                    print (i_atom)
                if len(i_atom) == 6:
                    Atom_index.append(int(i_atom[0]))
                    NumElement.append(int(i_atom[1]))
                    AtomicType.append(int(i_atom[2]))
                    X.append(float(i_atom[3]))
                    Y.append(float(i_atom[4]))
                    Z.append(float(i_atom[5]))
                    count += 1
                    continue
                else :
                    print ("Reading atom coordinates is finished...")
                    N = count-5
                    print ("Number of atoms: ", N)
                    count = 0
                continue


#Translating  atomic number to element symbol
    Mol_atom = []
    Mol_CartX = zeros(N)
    Mol_CartY = zeros(N)
    Mol_CartZ = zeros(N)

    for i in range(N):
        Mol_atom.append(GaussianRunPack.AtomInfo.AtomicNumElec(NumElement[i]))
        Mol_CartX[i] = X[i]
        Mol_CartY[i] = Y[i]
        Mol_CartZ[i] = Z[i]
#            print (Mol_atom[i])

#############
    del Atom_index[:]
    del NumElement[:]
    del AtomicType[:]
    del X[:]
    del Y[:]
    del Z[:]
    gc.collect()

    if outfile != None:
        Make_xyzfile(Mol_atom, Mol_CartX, Mol_CartY, Mol_CartZ, outfile , given_Charge, given_SpinMulti)

    return Mol_atom, Mol_CartX, Mol_CartY, Mol_CartZ


if __name__ == '__main__':

    usage = 'Usage; %s jobname' % sys.argv[0]

    try:
        infilename = sys. argv[1]
    except:
        print (usage); sys.exit()


    with open(infilename, 'r') as ifile:
        lines = ifile.readlines()

       
    print(Extract_Coordinate(lines))



