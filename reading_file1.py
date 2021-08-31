f = open('data.txt','rt')     #read text mode
# content = f.read()            #reading everything whatever remaning or from the initial of the paragraph.

# for line in content:          #print character by character in a new line. 
    # print(line)

for line in f: 
    print(line,end="")
f.close()

