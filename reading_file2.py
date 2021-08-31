f = open('data.txt','rt')     #read text mode

print(f.readline())
print(f.readline(),end="")

print(f.readline())

print(f.readlines())