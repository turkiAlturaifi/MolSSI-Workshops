import psi4
import numpy as np
import IPython

# Initial setup
psi4.set_memory('2 GB')
psi4.set_num_threads(2)

file_prefix = 'methane_HF-DZ'

ch4 = psi4.geometry("""
symmetry c1
0 1
   C       -0.85972        2.41258        0.00000
   H        0.21028        2.41258        0.00000
   H       -1.21638        2.69390       -0.96879
   H       -1.21639        3.11091        0.72802
   H       -1.21639        1.43293        0.24076
""")


# Geometry optimization
psi4.set_output_file(file_prefix + '_geomopt.dat', False)
psi4.set_options({'g_convergence': 'gau_tight'})
psi4.optimize('scf/cc-pVDZ', molecule=ch4)


# Run vibrational frequency analysis
psi4.set_output_file(file_prefix + '_vibfreq.dat', False)
scf_energy, scf_wfn = psi4.frequency('scf/cc-pVDZ', molecule=ch4, return_wfn=True, dertype='gradient')

IPython.embed()
# Save "raw" frequencies into a variable
rawfreq = scf_wfn.frequency_analysis['omega'][2]

# Eliminate imaginary parts of frequencies,
# round the frequencies (to the nearest whole number),
# and extract only the *non-zero* frequencies
roundnzfreq = np.round(np.real(rawfreq))[6:]


# Determine the unique non-zero frequencies and
# the number of times each such frequency occurs;
# store these in a NumPy array in the format:
# {frequency, count} (i.e, one line per freq.)
freqlist = np.array(np.unique(roundnzfreq, return_counts=True)).T

# Save the NumPy array with frequency and count data
# to a text file
np.savetxt('methane_freqlist.txt',freqlist, fmt='%0.1f,%d', delimiter=',', header = 'freq,degenrcy')
print('a new file: methane_freqlist.txt has been created with the frequncies and degenrcies')


