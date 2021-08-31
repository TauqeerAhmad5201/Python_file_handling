f = open('tell_function_text.txt','r+')
print(f.tell())  #tell us where the pointer is 
print(f.read())
print(f.tell())

f.write('\nStill learning man. :< :>')
print(f.tell())
f.close()