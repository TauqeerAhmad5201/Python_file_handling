# w+ = write first and then read aswell overrides the existing data
f = open('write_read.txt','w+')
print(f.tell())
f.write('Hey!?, Anyone who wants to hangout with me?')
print(f.tell())
print(f.read())   #if we put this function before the .write function so it's not gonna work and here the file pointer is simply at the end so it gonna print blank

f.seek(0)
print(f.read())
f.close()