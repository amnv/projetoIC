import glob
import gzip
import shutil

files = glob.glob("../data/err_files/*.txt.gz")
for fname in files:
    #defene file name
   ## print(fname)
    fname_out = fname.split(".gz")[0]
    fname_out = fname_out.replace("/err_files/", "/")
    print("Extraindo arquivo ", fname_out)

    with gzip.open(fname, 'rb') as f_in:
        with open(fname_out, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)