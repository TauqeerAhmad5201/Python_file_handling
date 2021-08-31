f = open('data.txt','rt')     #read text mode

content = f.read(4)          #reading 4 characters 
print(content)

content = f.read(8)          #reading 8 characters after those 4 characters
print(content)

content = f.read()           #reading whole line wtherver remaning or from the initial of the paragraph.
print(content)

content = f.read()
print('2',content)           #.read() has already read out the remaining content 
f.close()