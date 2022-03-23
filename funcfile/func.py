import os
import sys


def GetFile(path):
    files=os.listdir(path)
    file_list=[]
    for file in files:
        if os.path.isfile(os.path.join(path,file)):
           file_list.append(os.path.join(path,file))
    return file_list


def CheckFile(path,filename):
    files = os.listdir(path)

    filelink = path+r"\\" + filename
 #   print(filelink)
    FileCheck = os.path.exists(filelink)

#    for file in files:
#        print(file,type(file))
#        if file == 'dailyrate.csv':
#            FileCheck == 'T'
    return FileCheck
            




filename='dailyrate.csv'
path=sys.path[0]
a=CheckFile(path,filename)
print(a)

#print(path,"*根目录文件夹内容：")
#for name in b:
#    print("~",os.path.join(path,name))
#for name in a:
#    print(os.path.join(path,name))
# 
#for root,dirs,files in os.walk(path,topdown=True):
#    for name_dir in dirs:
#        a=GetFile(os.path.join(root,name_dir))
#        b=GetDirectory(os.path.join(root,name_dir))
#        print("")
#        print(os.path.join(root,name_dir),"文件夹内容：")
#        for name_cdir in b:
#            print("~",os.path.join(root,name_dir,name_cdir))
#        for name_file in a:
#            print(os.path.join(root,name_dir,name_file))