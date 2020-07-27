import sys

#Get first param as file to decode
file = sys.argv[1]

#Read xored file
f = open(file,"r")
data = f.read()
f.close()
datalenght = len(data)

#Get first string (until character 0x00)
XorKey = data.split(chr(0x0))[0]
XorKeyLen = len(XorKey)

res = ""

#Decode the rest of the file with the xor key
for i in range(datalenght - XorKeyLen -1):
	res+= chr( ord(data[i+XorKeyLen+1])^ ord(XorKey[i%XorKeyLen]) )

#Save the decoded file
fr = open("plugx.exe","w")
fr.write(res)
fr.close()
