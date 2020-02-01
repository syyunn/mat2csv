## Env Setting
`python v.3.8`

## Latest `.Mat` Documentation

[official](https://www.mathworks.com/help/matlab/import_export/mat-file-versions.html?searchHighlight=.mat&s_tid=doc_srchtitle)

### Latest & Default Versioning of .Mat as of 2020 
`v.7.x.x. 

`.mat` describes its internal data representation with `level` and current lateset version 7 corresponds to `level 5`. Refer to [this](https://www.loc.gov/preservation/digital/formats/fdd/fdd000440.shtml)

### Integration into Javascript 
Since `.mat` uses [hdf5](https://portal.hdfgroup.org/display/HDF5/HDF5), consider to consume the data in-memory using exisitng `hdf5` related js-libs without passing-through the api.

Consider reading `.mat`'s binary directly according to the format of the `.mat` as documented [here](https://www.mathworks.com/help/pdf_doc/matlab/matfile_format.pdf)
