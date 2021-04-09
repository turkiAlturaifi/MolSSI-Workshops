import os
import argparse as argp

if __name__=='__main__':

    parser = argp.ArgumentParser(description="This script gives the user the Etot energy values.")
    parser.add_argument("mdout_file", help="The filepath for the mdout file to analyze.",nargs='*')

    args = parser.parse_args()

    file = args.mdout_file



for f in file:
    outfile=open(f,'r')
    data=outfile.readlines()
    outfile.close()
    f_name=os.path.basename(f).split('.')[0]

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
'''
# their solution
import os
import argparse

# Get filename from argparse

parser = argparse.ArgumentParser("This script parses amber mdout file to extract the total energy.")

parser.add_argument("path", help="The filepath of the file to be analyzed.", nargs='*')

args = parser.parse_args()

filenames = args.path

for filename in filenames:

    # Figure out the file name for writing output
    fname = os.path.basename(filename).split('.')[0]

    # Open the file.

    f = open(filename, 'r')

    # Read the data.
    data = f.readlines()

    # Close the file.
    f.close()

    etot = []
    # Loop through lines in the file.
    for line in data:
    # Get information from lines.
        split_line = line.split()

        if 'Etot' in line:
            #print(split_line[2])
            etot.append(f'{split_line[2]}')
    values = etot[:-2]

    # Open a file for writing
    outfile_location = F'{fname}_Etot.txt'
    outfile = open(outfile_location, 'w+')

    for value in values:
        outfile.write(f'{value}\n')

    outfile.close()
'''