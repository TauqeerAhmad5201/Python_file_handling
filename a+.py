#NO OVERWRITE --> APPENDING DATA AND THEN READ IT
f = open('appending+.txt','a+')
print(f.tell())
f.write('Hey, I think there is a progress.')
f.seek(0)
print(f.read())
f.close()

#funny fact ---> remember whenever append/write the data to the previous one(not overwriting) then new line is used then after that no auto new line is provided.