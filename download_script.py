import pandas as pd
import urllib.request

#build dataframe
df = pd.read_csv("ponteiros.csv")

#defining values to download
valores = df.iloc[1][1:]

print('Beginning file download with urllib2...')

for item in valores:
    dir_name = item[:5] + "nnn"
    print("downloading file ", item)
    url = "https://ftp.ncbi.nlm.nih.gov/geo/series/{0}/{1}/matrix/{1}_series_matrix.txt.gz".format(dir_name, item)
    file_name = "{0}_series_matrix.txt.gz".format(item)
    urllib.request.urlretrieve(url, file_name)  

print("downloads finalizados")