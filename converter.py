import scipy.io
import numpy as np

data = scipy.io.loadmat("subject.mat")

for i in data:
	if '__' not in i and 'readme' not in i:
		np.savetxt(("filesforyou/"+i+".csv"),data[i],delimiter=',')

if __name__ == "__main__":
    pass