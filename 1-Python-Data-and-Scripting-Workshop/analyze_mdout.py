'''
For this homework assignment, you will return to your first project where you processed the file 03_Prod.mdout.
Create a command line script using argparse which can take in an mdout file from Amber, pull out total energy for each time step,
and write a new file containing these values. The script should take a file name (03_Prod.mdout)
and output a file with the names filename_Etot.txt. Modify your week 1 homework to do this.

In the first project, the file we wrote had two values at the end which we did not want for the total energy.
The last two values were some statistics associated with the md simulation and were not total energies.

Your assignment is to parse this file, and write a new file containing a list of the > total energies.
Name your file Etot.txt. When you open it, it should look like this:

# open the file after defining the path
file_name=os.path.join('data','03_prod.mdout')
outfile=open(file_name,'r')
data=outfile.readlines()
outfile.close()

# write to a file
datafile=open('03_prod_energies.txt','w+')

#read lines
for line in data:
    if 'Etot  ' in line:
        words=line.split()
        #energy=words[2]
        datafile.write(F'{words[2]} \n')
datafile.close()

'''

import os
import argparse as argp


# open the file after defining the path
def open_mdout(file):
    #file_name=os.path.join('data','03_prod.mdout')
    outfile=open(file,'r')
    data=outfile.readlines()
    outfile.close()

    f_name=os.path.basename(file).split('.')[0]

    # write to a file
    datafile=open(f_name+'_Etot.txt','w+')



    #read lines
    for line in data:
        if 'Etot  ' in line:
            words=line.split()
            #energy=words[2]
            if '-' in words[2]: #removing the last one
                datafile.write(F'{words[2]} \n')
    datafile.close()

if __name__=='__main__':
    parser = argp.ArgumentParser(description="This script gives the user the Etot energy values.")
    parser.add_argument("mdout_file", help="The filepath for the mdout file to analyze.")

    args = parser.parse_args()

    file = open_mdout(args.mdout_file)

'''
their solution:

import os
import glob
import argparse


if __name__ == "__main__":

    # Create the argument parser
    parser = argparse.ArgumentParser("This script parses amber mdout files to extract the total energy.")
    parser.add_argument("path", help="The filepath to the file(s) to be analyzed.")

    args = parser.parse_args()
    filename = args.path

    # Read the data from the specified file.
    f = open(filename)
    data = f.readlines()
    f.close()

    # Figure out the file name for writing the output.
    fname = os.path.basename(args.path).split('.')[0]

    etot = []
    # Loop through the lines
    for line in data:
        split_line = line.split()
        if 'Etot' in line:
            etot.append(float(split_line[2]))

    # Get rid of values we don't need.
    values = etot[:-2]

    # Open a file for writing
    outfile_location = F'{fname}_Etot.txt'
    outfile = open(outfile_location, 'w+')

    for value in values:
        outfile.write(f'{value}\n')

    outfile.close()
'''


