com_file = open("comtext.txt","r") #r: read, w:write, r+:read and write
# print(com_file.read())
# print(com_file.readlines()[2]) # readline: Read single line, readlines: Read all lines

for boss in com_file.readlines():
    print(boss)
com_file.close()