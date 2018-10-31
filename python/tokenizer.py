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
            aux_list = line.split("\t")[1:]
            for aux in aux_list:
                processed_lines.append(aux.split("\n")[0])
    
    return processed_lines

def remove_small_text(lines, threshold = 3):
    ret = []
    for line in lines:
        if len(line.split(" ")) > threshold:
            ret.append(line)
    
    return ret

def change_name_csv_file(name):
    ret = name.split("/")[-1]
    ret = ret.split(".txt")[0]
    return "../data/processed_text/" + ret + ".csv"

def change_name_txt_file(name, number_line):
    ret = name.split("/")[-1]
    ret = ret.split(".txt")[0]
    return "../data/processed_text/" + ret + "_" + str(number_line) + ".txt"

def savingCSVs(file, output_file_name):
    print("Salvando em csv")
    output_file_name = change_name_csv_file(file)
    with open(output_file_name , "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in processed_lines:
            writer.writerow([val])


#Read and preprocess text files
files = glob.glob("../data/*.txt")
for file in files:
    text = open(file, "r")
    splited_text = split_lines(text)
    untagged_text = remove_tag(splited_text)
    processed_lines = remove_small_text(untagged_text)

    #export as csv
    #savingCSVs(file, output_file_name)
    
    #export as files .txt
    for line in range(len(processed_lines)):
        output_file_name = change_name_txt_file(file, line)
        with open(output_file_name , "w") as output:
            output.write(processed_lines[line])