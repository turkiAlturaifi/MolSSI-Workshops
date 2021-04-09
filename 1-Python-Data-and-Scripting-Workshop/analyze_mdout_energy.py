import os
import argparse as argp
import matplotlib.pyplot as plt

if __name__=='__main__':

    parser = argp.ArgumentParser(description="This script gives the user the Etot energy values.")
    parser.add_argument("mdout_file", help="The filepath for the mdout file to analyze.",nargs='*')
    parser.add_argument("-plot", help="plot energies",default=True)

    args = parser.parse_args()

    file = args.mdout_file


Etot=[]
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
                Etot.append(float(words[2]))
    datafile.close()

    if args.plot is True:
        plt.plot(Etot)
        plt.savefig(f_name+'.png',dpi=300)
