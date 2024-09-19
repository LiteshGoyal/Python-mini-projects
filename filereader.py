import os
path  = input("path:")
os.chdir(path)

user = input("name:")
a  = user + ".txt"
if os.path.exists(a):
    f = open(a,'r')
    c = f.read()
    print(c)
    f.close()
else:
    print("ERROR")