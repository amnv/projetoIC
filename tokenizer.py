import csv
import glob

#limpando dados
def split_lines(text):
    print("separando o texto por linha")
    lines = []
    for i in text:
        if ("!series_matrix_table_begin") in i:
            print("separação por linha finalizada")
            break

        lines.append(i)
        
    return lines

def remove_tag(lines):
    processed_lines = []
    print("removendo tags")
    for line in lines:
        if not line.startswith("\n"):
            processed_lines.append(line.split("\t")[1].split("\n")[0])
    
    return processed_lines


#Read and preprocess text files
files = glob.glob("data/*.txt")
for file in files:
    text = open(file, "r")
    splited_text = split_lines(text)
    untagged_text = remove_tag(splited_text)

    #export as csv
    print("Salvando em csv")
    aux = file.split(".")
    output_file = aux[0] + ".csv"
    with open(output_file , "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in untagged_text:
            writer.writerow([val])
