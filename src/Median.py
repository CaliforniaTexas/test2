import os
import sys
os.system('cls')
import statistics
import glob

file_lines=[]
Wcnt=[]
m=[]
#sys.stdout = open("C:\\Users\\SIVA\\Desktop\\Median_res.txt","w")

list_of_files = glob.glob("C:\\Users\\SIVA\\Desktop\\Code\\wc_input\\Textfiles\\*.txt")
#f = open("C:\\Users\\SIVA\\Desktop\\Proj\\output\\Median.txt", "a")
for file in sorted(list_of_files):
    with open(file, 'r') as content_file:
        file_read=content_file.read()
        file_lines.append(file_read)
#print(file_lines)

for line_lf in file_lines:
    lineIn = line_lf.split('\n')
    for line in lineIn:
#        print(line)
        word = line.split()
        Wcnt.append(len(word))
        m.append(statistics.median(Wcnt))
#        print(m)

f=open("C:\\Users\\SIVA\\Desktop\\Code\\wc_output\\Median_res.txt","w")
f.write(str(m).replace(',','\n').replace('[','').replace(']','').replace(' ',''))
f.close()

