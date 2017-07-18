#!/usr/bin/python
import sys, csv, glob, math

name_list = glob.glob("./text_data/*.fpkm")
# print name_list

data_ex = open(name_list[0],'r')
transcript = []
data_ex.readline() #cut off the header
data_ex.readline() #cut data header
for line in data_ex:  #create the tissue_id column
    line = line.strip()
    if len(line) != 0:
        columns = line.split('\t')
        first_col = str(columns[0])
        transcript.append(first_col)
print len(transcript)

# with open("corex_data.csv",'w') as resultFile:
#     wr = csv.writer(resultFile)
#     wr.writerows([transcript])

for i in name_list:
    data = open(i, 'r')
    # print name_list[0]

    header = data.readline() #cut off the header
    header2 = data.readline() #cut data header
    # print header

    fpkm = []
    for line in data:
        line = line.strip()
        if len(line) != 0:
            columns = line.split('\t')
            sixth_col = int(math.floor(float(columns[5])))
            fpkm.append(sixth_col)
            # print columns[5]
    # print fpkm
    print "count the data :"+str(len(fpkm))
# print "count the transcript :"+str(len(transcript))
# print transcript

    # with open("corex_data.csv",'a') as resultFile:
    #     wr = csv.writer(resultFile)
    #     wr.writerows([fpkm])
