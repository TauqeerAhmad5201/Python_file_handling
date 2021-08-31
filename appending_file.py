f = open('appended_data.txt','a')
f.write('Hey, see the new data has been added.')
f.close()
#open and read the file after the appending:
f = open('appended_data.txt','r')
print(f.read())
f.close()
