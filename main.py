import os
import re

path = input("Please enter your path: ")

files = os.listdir(path)

names = [] 


for file in files:
    name = re.findall("[\S]+S[\d]+E[\d]+", file)
    names.append(name[0])

for name in names:
    for j in reversed(range(len(name))):
        if name[j] == '.':

            print(name[:j])
            print(name[j + 1:])
            break


