import scipy.io
import pandas as pd

fpath = './burgers_shock.mat'

mat = scipy.io.loadmat(fpath)
mat_dict = {k: v for k, v in mat.items() if k[0] != '_'}
data = pd.DataFrame({k: pd.Series(v[0]) for k, v in mat_dict.items()})
data.to_csv("example.csv")

if __name__ == "__main__":
    pass

