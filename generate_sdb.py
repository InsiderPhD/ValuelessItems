import csv

copy_me =""
copy_me+="defwords(["
with open('itemsheet.csv', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        for value in row:
            copy_me+="\""+value+"\","
copy_me+="],\"red\");"

with open("sdb_defwords.txt", "w") as text_file:
    text_file.write(copy_me)