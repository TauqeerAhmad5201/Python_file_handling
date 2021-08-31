#r+ = First Open for reading and then writing
f = open('reading_and_writing.txt','r+')
print(f.read())
f.write('Do I love programming?')
f.close()