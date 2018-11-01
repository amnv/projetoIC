import pandas as pd
import urllib.request

#build dataframe
df = pd.read_csv("../ponteiros.csv", header=None)

#defining values to download
valores = df[0].unique()

print('Beginning file download...')
download_fail = []
for item in valores:
    dir_name = item[:5] + "nnn"
    print("downloading file ", item)
    try:
        url = "https://ftp.ncbi.nlm.nih.gov/geo/series/{0}/{1}/matrix/{1}_series_matrix.txt.gz".format(dir_name, item)
        file_name = "../data/{0}_series_matrix.txt.gz".format(item)
        urllib.request.urlretrieve(url, file_name)  
    except Exception:
        print("arquivo não localizado")
        download_fail.append(item)

print("downloads finalizados")

#build file to sabe err
log_err = open("../log_err.txt", "w")
for i in download_fail:
    log_err.write(i + "\n")
log_err.close()