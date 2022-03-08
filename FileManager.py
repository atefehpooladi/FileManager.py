import os
import glob
files_list=glob.glob("*")
extention_set=set()
for each_file in files_list:
    #if "." in each_file:
    try:
        extention=each_file.split(".")[1]
        extention_set.add(extention)
    except:
        continue
def create_folders():
    for ext in extention_set:
        if ext == "py":
            continue
        try:
            os.makedirs(ext+"_Folders")
        except:
            continue
#create_folders()
def move_Files():
    for each_file in files_list:
        try:
            extention=each_file.split(".")[1]

            os.rename(each_file,extention+"_Folders/"+each_file)
        except:
            continue
create_folders()
move_Files()