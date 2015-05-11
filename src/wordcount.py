import re,os
import string
file=open("C:\\Users\\SIVA\\Desktop\\Code\\wc_input\\Wordcount.txt","r+").read()
word_count={}
for word in file.lower().split():
    if word not in word_count:
        word_count[word]=1

    else:
            word_count[word]+=1

for item in word_count.items():
    print ("{}\t{}".format(*item))

f=open("C:\\Users\\SIVA\\Desktop\\Code\\wc_output\\wc_result.txt","w")
for key,value in sorted(word_count.items()):
    f.write(key)
    f.write("\t") 
    f.write(str(value))
    f.write("\n") 

for item in sorted(word_count.items()):
    f.write("{}\t{}\n".format(*item))    
f.close()
