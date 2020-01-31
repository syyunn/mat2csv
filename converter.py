import csv

import scipy.io

fpath = './burgers_shock.mat'

mat = scipy.io.loadmat(fpath)
keys = [key for key in mat.keys() if '_' not in key]

mat_dict = {k: v for k, v in mat.items() if k[0] != '_'}

with open('example.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.writer(f)
    w.writerows(mat_dict.items())


if __name__ == "__main__":
    pass

