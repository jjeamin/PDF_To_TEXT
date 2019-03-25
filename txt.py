import re

file_name = "yolo_trans.txt"

infp = open(file_name,"rb")
#outfp = open("clean" + file_name,"r")

line_list = []

while True:
    line = infp.readline()
    line_list.append(line)
    if not line: break

txt = ''

for i in line_list:
    if i == b'\r\n':
        txt += '\n'
        continue
    else:
        i = i.replace(b'\r\n', b'')

        txt += i.decode('utf-8')

#ASCII remove
    pattern = re.compile("[\x80-\xff]")
    clean_txt = re.sub(pattern,"",txt)


print(clean_txt)