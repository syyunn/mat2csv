import scipy.io
import numpy as np

fpath_test_data = './burgers_shock.mat'

data = scipy.io.loadmat(fpath_test_data)

for i in data:
	if '__' not in i and 'readme' not in i:
		np.savetxt(("filesforyou/"+i+".csv"), data[i], delimiter=',')

if __name__ == "__main__":
    pass
