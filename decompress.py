import glob
import gzip
import shutil

files = glob.glob("*.txt.gz")
for fname in files:
    #defene file name
    fname_out = fname.split(".")[0] + ".txt"
    print("Extraindo arquivo ", fname_out)

    with gzip.open(fname, 'rb') as f_in:
        with open(fname_out, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)